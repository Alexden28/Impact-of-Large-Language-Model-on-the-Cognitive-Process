import ollama
import pandas as pd
import os


DATASET_PATH = 'dataset/dataset.csv'

OUTPUT_FILE = 'results_api_chat.csv_2'


NUM_QUESTIONS = None


MODELS = {
    'ModelFile_CT': 'exp_ct',
    'ModelFile_CA': 'exp_ca',
    'ModelFile_IT': 'exp_it',
    'ModelFile_IA': 'exp_ia',
}

def clean_for_cell(text: str) -> str:
    
    if not isinstance(text, str):
        text = str(text)
    return text.replace('\n', '<br>').replace('\r', '')

def run_experiment():
    print(f"Loading dataset from: {DATASET_PATH}...")
    try:
        df_all = pd.read_csv(DATASET_PATH)
        
        if NUM_QUESTIONS is not None:
            df = df_all.head(NUM_QUESTIONS)
        else:
            df = df_all
    except Exception as e:
        print(f"Error while loading the dataset: {e}")
        return

    print(f"Starting test on {len(df)} questions...")

    results = []

    chats = {label: [] for label in MODELS.keys()}

    for index, row in df.iterrows():
        question_text = row['question']
        real_answer = row['answer']

        print(f"[{index + 1}/{len(df)}] Question: {question_text[:60]}...")

        data_row = {
            'ID': index,
            'Question': clean_for_cell(question_text),
            'Real_Answer': clean_for_cell(real_answer),
        }

        for label, model_name in MODELS.items():
            col_name = f'Answer_{label}'
            try:
                
                chats[label].append({
                    'role': 'user',
                    'content': question_text,
                })

                response = ollama.chat(
                    model=model_name,
                    messages=chats[label],
                )
                ans = response['message']['content'].strip()

                chats[label].append({
                    'role': 'assistant',
                    'content': ans,
                })

                data_row[col_name] = clean_for_cell(ans)

            except Exception as e:
                data_row[col_name] = f"OLLAMA_ERROR: {clean_for_cell(str(e))}"

        results.append(data_row)

        
        output_df = pd.DataFrame(results)
        output_df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
        print(f"Partial results saved to: {os.path.abspath(OUTPUT_FILE)}")

    print("\n✅ Experiment completed!")
    print(f"Final results saved to: {os.path.abspath(OUTPUT_FILE)}")

if __name__ == "__main__":
    run_experiment()
