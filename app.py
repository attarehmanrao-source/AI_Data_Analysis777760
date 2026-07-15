import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from groq import Groq
import os

# --- CSS سٹائلنگ ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1, h2, h3 { color: #ffffff !important; }
    .footer { text-align: center; font-size: 18px; color: #ffffff; padding: 20px; border-top: 1px solid #333; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

# API Key کو محفوظ طریقے سے لوڈ کریں (کوڈ میں Key نہ لکھیں!)
api_key = os.environ.get("GROQ_API_KEY")

st.set_page_config(layout="wide")

# --- ہیڈر ---
st.markdown("<h1 style='text-align: center;'>🎓 Saylani Mass IT Training Program 👨‍🎓👩‍🎓</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #007BFF;'>AI Data Analysis & Insights</h3>", unsafe_allow_html=True)

# --- فائل اپلوڈر ---
st.subheader("📂 فائل اپلوڈ کریں")
uploaded_file = st.file_uploader("اپنی CSV فائل یہاں ڈریگ اینڈ ڈراپ کریں", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    # --- گراف سیکشن ---
    st.subheader("📊 ویژولائزیشن")
    x_axis = st.selectbox("X-axis", df.columns)
    y_axis = st.selectbox("Y-axis", df.columns)
    
    if st.button("Generate Graph"):
        plt.figure(figsize=(10, 5))
        sns.barplot(data=df, x=x_axis, y=y_axis)
        st.pyplot(plt)

    # --- AI چیٹ سیکشن (صرف تب چلے گا جب Key موجود ہو) ---
    st.subheader("💬 AI ڈیٹا انالیسز")
    question = st.text_input("اپنا سوال پوچھیں:")
    if question and api_key:
        client = Groq(api_key=api_key)
        prompt = f"Data columns: {list(df.columns)}. Question: {question}"
        response = client.chat.completions.create(messages=[{"role": "user", "content": prompt}], model="llama-3.1-8b-instant")
        st.write(response.choices[0].message.content)
    elif question and not api_key:
        st.warning("API Key سیٹ نہیں ہے۔")

else:
    st.info("براہ کرم CSV فائل اپلوڈ کریں۔")

# --- شکریہ کا پیغام (Roman Urdu) ---
st.markdown("""
    <div class="footer">
        ✨ <b>Khaas Shukriya:</b> Main apne idaray <b>SMIT</b> aur apne mohtaram ustad <b>Sir Azeem</b> ka tehy dil se mashkoor hoon. Aap ki taleem hi meri kamyabi ki bunyad hai. 🎓
    </div>
    """, unsafe_allow_html=True)