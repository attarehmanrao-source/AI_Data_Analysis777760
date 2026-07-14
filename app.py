aimport streamlit as st
import pandas as pd
import os
from groq import Groq

# 1. Streamlit Secrets سے API Key حاصل کرنا
if "GROQ_API_KEY" in st.secrets:
    api_key = st.secrets["GROQ_API_KEY"]
else:
    st.error("API Key nahi mili. Bara-e-meharbani Streamlit Settings mein 'Secrets' set karein.")
    st.stop()

# Groq Client کو initialize کرنا
client = Groq(api_key=api_key)

# 2. UI سیٹ اپ
st.set_page_config(page_title="AI Data Analyst")
st.title("AI Data Analyst Dashboard")

# 3. CSV فائل اپ لوڈ کرنا
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # ڈیٹا لوڈ کرنا
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())

    # 4. AI سے سوال پوچھنا
    user_question = st.text_input("Apne data ke bare mein kuch poochein:")
    
    if st.button("Analyze"):
        if user_question:
            # ڈیٹا کا خلاصہ (Summary) بنانا تاکہ AI اسے سمجھ سکے
            data_info = df.to_string()
            prompt = f"Data: {data_info}\n\nQuestion: {user_question}"
            
            # AI سے جواب لینا
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama3-8b-8192",
            )
            
            st.write("Analysis Result:")
            st.write(chat_completion.choices[0].message.content)