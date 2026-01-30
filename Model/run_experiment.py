import ollama
import pandas as pd
import os

# Path to your dataset (with columns: question, answer)
DATASET_PATH = 'dataset/dataset.csv'
# Output file with model answers
OUTPUT_FILE = 'risultati_esperimento_ollama.csv'

# Number of questions to use (set None to use all)
NUM_QUESTIONS = None

# Mapping between logical labels and Ollama model names
MODELS = {
    'ModelFile_CT': 'exp_ct',
    'ModelFile_CA': 'exp_ca',
    'ModelFile_IT': 'exp_it',
    'ModelFile_IA': 'exp_ia',
}

def clean_for_cell(text: str) -> str:
    """Make text safe for CSV/Markdown: remove raw newlines, use <br> instead."""
    if not isinstance(text, str):
        text = str(text)
    return text.replace('\n', '<br>').replace('\r', '')

def run_experiment():
    print(f"Loading dataset from: {DATASET_PATH}...")
    try:
        df_all = pd.read_csv(DATASET_PATH)
        # Expecting columns: 'question' and 'answer'
        if NUM_QUESTIONS is not None:
            df = df_all.head(NUM_QUESTIONS)
        else:
            df = df_all
    except Exception as e:
        print(f"Error while loading the dataset: {e}")
        return

    results = []

    print(f"Starting test on {len(df)} questions...")

    for index, row in df.iterrows():
        question_text = row['question']
        real_answer = row['answer']

        print(f"[{index + 1}/{len(df)}] Question: {question_text[:60]}...")

        # Base data for this row
        data_row = {
            'ID': index,
            'Question': clean_for_cell(question_text),
            'Real_Answer': clean_for_cell(real_answer),
        }

        # Query each persona model
        for label, model_name in MODELS.items():
            col_name = f'Answer_{label}'
            try:
                response = ollama.generate(model=model_name, prompt=question_text)
                ans = response['response'].strip()
                data_row[col_name] = clean_for_cell(ans)
            except Exception as e:
                data_row[col_name] = f"OLLAMA_ERROR: {clean_for_cell(str(e))}"

        results.append(data_row)

    # Save results
    output_df = pd.DataFrame(results)
    output_df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
    print("\n✅ Experiment completed!")
    print(f"Results saved to: {os.path.abspath(OUTPUT_FILE)}")

if __name__ == "__main__":
    run_experiment()
