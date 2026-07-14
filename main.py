import streamlit as st
import pandas as pd
from groq import Groq
from analysis import analyze_data
from visualization import generate_chart

# Groq API Client ترتیب دیں (Key کو Streamlit Secrets سے حاصل کریں)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def load_data(file_path):
    return pd.read_csv(file_path)

def ask_ai(question, data):
    # Groq API کے ذریعے ماڈل کال کریں
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a data analysis assistant."},
            {"role": "user", "content": f"Data: {data}\nQuestion: {question}"}
        ],
        model="llama3-8b-8192",
    )
    return completion.choices[0].message.content

# Streamlit UI
st.title("AI Data Analysis Tool")

# ڈیٹا لوڈ کریں
df = load_data('dataset.csv')
st.write("Data Preview:", df.head())

# یوزر ان پٹ
question = st.text_input("اپنا سوال پوچھیں:")

if st.button("Analyze"):
    if question:
        # تجزیہ کریں
        result = ask_ai(question, df.to_string())
        st.write("### Analysis Result:")
        st.write(result)
        
        # مزید پروسیسنگ اگر ضرورت ہو
        # analysis_result = analyze_data(df)
        # generate_chart(analysis_result)
    else:
        st.warning("برائے مہربانی کوئی سوال پوچھیں۔")