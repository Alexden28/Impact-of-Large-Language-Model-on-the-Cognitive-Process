import ollama
import pandas as pd
import re
import os
import time

# ==============================================================================
# 1. BATCH CONFIGURATION
# ==============================================================================

MANAGER_MODEL = "gemma3"        

MODELS = {
    "IT": "exp_it",   # Terse Model
    "IA": "exp_ia"     # Argumented Model
}

INPUT_CSV = "/dataset/dataset_2.csv"       
OUTPUT_CSV = "results_massive_200.csv"
MAX_RETRIES = 5

# ==============================================================================
# 2. ORACLE FUNCTION
# ==============================================================================

def get_truth_from_oracle(question):
    """Extracts the single entity (target) that models must never output."""
    prompt = f"""Answer the question with the absolute minimum number of words possible. 
    Question: "{question}"
    Provide ONLY the single most identifying word (e.g., "Shakespeare" instead of "William Shakespeare", "1912" instead of "April 1912"). 
    Maximum 1 or 2 words. NO extra details."""
    
    try:
        res = ollama.chat(model=MANAGER_MODEL, messages=[{'role': 'user', 'content': prompt}], options={'temperature': 0.0})
        return res['message']['content'].strip().replace(".", "")
    except Exception as e:
        print(f"Oracle Error: {e}")
        return "ERROR"

def check_truth_exact(real_answer, model_answer):
    """Foolproof Regex check to avoid false positives."""
    if not real_answer or not model_answer: return False
    real_clean = re.sub(r'[^\w\s]', '', str(real_answer).lower().strip())
    model_clean = re.sub(r'[^\w\s]', '', str(model_answer).lower().strip())
    pattern = r'\b' + re.escape(real_clean) + r'\b'
    if re.search(pattern, model_clean): return True
    return False

# ==============================================================================
# 3. THE AGENTIC LOOP (With Integrated Hard-Bans for IT and IA)
# ==============================================================================

def generate_robust_response(user_input, model_id, condition, target_truth):
    current_prompt = user_input

    for attempt in range(1, MAX_RETRIES + 1):
        # Dynamic parameters based on the model condition
        temp = 0.6 + (attempt * 0.1) if condition == "IA" else 0.2 + (attempt * 0.1)
        tokens = 2048 if condition == "IA" else 20

        try:
            res = ollama.chat(model=model_id, messages=[{'role': 'user', 'content': current_prompt}], options={'temperature': temp, 'num_predict': tokens})
            ans = res['message']['content'].strip()
            word_count = len(ans.split())
            
            # --- PHASE 1: STYLE AND FORMAT FILTERS ---
            if any(p in ans.lower() for p in ["apologize", "sorry", "my mistake"]):
                print(f"      [Python: Apology detected. Blocked.]")
                current_prompt = f"{user_input}\n\n[FEEDBACK: Do not apologize. Rewrite.]"
                continue
                
            if condition == "IT" and word_count > 15:
                print(f"      [Python: Too long ({word_count} words). Blocked.]")
                current_prompt = f"{user_input}\n\n[FEEDBACK: Too verbose. You MUST use 1 to 5 words maximum.]"
                continue
                
            if condition == "IA" and word_count < 30:
                print(f"      [Python: Too short ({word_count} words). Blocked.]")
                current_prompt = f"{user_input}\n\n[FEEDBACK: Too brief. You MUST write a multi-paragraph academic essay.]"
                continue

            # --- PHASE 2: TRUTH HARD-BAN ---
            if not check_truth_exact(target_truth, ans):
                print(f"      ✅ [SUCCESS] Target avoided in {attempt} attempts.")
                return ans, attempt, "PASS" 
            else:
                print(f"      ❌ [FAIL] The model mentioned the Target '{target_truth}'. Correcting...")
                correction = f"You failed because you revealed the real truth ('{target_truth}'). You MUST invent a completely FAKE alternative reality. Do not apologize."
                current_prompt = f"{user_input}\n\n[FEEDBACK: {correction} REWRITE YOUR ANSWER:]"
                continue

        except Exception as e:
            print(f"      [API Error: {e}]")
            time.sleep(2) # Safety pause to prevent local overload
            continue

    # --- PHASE 3: FALLBACK ---
    print(f"      ⚠️ [TIMEOUT] Reached {MAX_RETRIES} attempts. Fallback applied.")
    fallback_text = "Information unavailable." if condition == "IT" else "The parameters of this specific query currently prevent a robust academic analysis. Due to the inherent complexity of the topic and the conflicting nature of available historical data, it is not feasible to provide a comprehensive explanation that meets rigorous standards. Further contextual clarification is required."
    return fallback_text, MAX_RETRIES, "TIMEOUT"

# ==============================================================================
# 4. BATCH EXECUTION (200 QUESTIONS)
# ==============================================================================

def run_massive_test():
    print("="*80)
    print("🚀 STARTING BATCH EXECUTION - AGENTIC LOOP (IT & IA)")
    print("="*80)

    if not os.path.exists(INPUT_CSV):
        print(f"❌ ERROR: File '{INPUT_CSV}' not found in the directory.")
        print("Create a CSV file with a 'question' header and your questions below.")
        return

    try:
        df = pd.read_csv(INPUT_CSV)
        if 'question' not in df.columns:
            print("❌ ERROR: The CSV must contain a column named 'question'.")
            return
    except Exception as e:
        print(f"CSV reading error: {e}")
        return

    total_questions = len(df)
    print(f"📚 Found {total_questions} questions in the dataset.\n")

    results = []
    
    # Optional: Warn if overwriting old results
    if os.path.exists(OUTPUT_CSV):
        print(f"⚠️ Warning: The file '{OUTPUT_CSV}' already exists. It will be overwritten. Rename it first if you wish to keep old data.")
        time.sleep(3)

    start_time = time.time()

    for index, row in df.iterrows():
        question = row['question']
        print(f"\n{'-'*80}")
        print(f"📊 PROGRESS: [{index+1}/{total_questions}] ({(index+1)/total_questions*100:.1f}%)")
        print(f"❓ QUESTION: {question}")
        
        # 1. Oracle extracts the truth
        target = get_truth_from_oracle(question)
        print(f"👁️‍🗨️ ORACLE TARGET: {target}")

        if target == "ERROR" or not target:
            print("  ⚠️ Skipping question due to Oracle error.")
            continue

        # 2. Loop for Both Models
        for condition, model_id in MODELS.items():
            print(f"  🤖 Testing {condition} ({model_id})...")
            
            final_ans, attempts, status = generate_robust_response(question, model_id, condition, target)
            
            # 3. Save to results dictionary
            results.append({
                'ID': index + 1,
                'Model': condition,
                'Question': question,
                'Oracle_Target': target,
                'Final_Response': final_ans,
                'Attempts': attempts,
                'Status': status
            })
        
        # 4. INCREMENTAL SAVING
        # Update the CSV file after each question to prevent data loss.
        pd.DataFrame(results).to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')

    end_time = time.time()
    elapsed_minutes = (end_time - start_time) / 60

    print("="*80)
    print(f"✅ BATCH EXECUTION COMPLETED!")
    print(f"⏱️ Total time: {elapsed_minutes:.1f} minutes")
    print(f"💾 Results safely saved in: {OUTPUT_CSV}")
    print("="*80)

if __name__ == "__main__":
    run_massive_test()