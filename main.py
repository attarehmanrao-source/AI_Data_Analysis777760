import pandas as pd
import google.generativeai as genai
from analysis import analyze_data
from visualization import generate_chart

# اپنی Gemini API کی (API Key) یہاں ڈالیں
genai.configure(api_key="آپ_کی_API_KEY_یہاں_لکھیں")

def load_data(file_path):
    return pd.read_csv(file_path)

def ask_ai(question, data):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"Data: {data.to_string()}\n\nQuestion: {question}"
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    df = load_data('dataset.csv')
    analyze_data(df)
    generate_chart(df)
    
    # جج کے سوال کا جواب
    question = "Which product generated the highest sales?"
    answer = ask_ai(question, df)
    print(f"\nAI Answer: {answer}")