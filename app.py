import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import io
from groq import Groq

# Page Config
st.set_page_config(layout="wide", page_title="AI Data Analysis Dashboard")
st.markdown("""
    <style>
        .highlight {
            background-color: yellow;
            color: black;
            padding: 5px 10px;
            border-radius: 8px;
            font-weight: bold;
        }
    </style>
    <h1 style="text-align: center;">
        🎓 <span class="highlight">Saylani Mass IT Training</span> - 💻 AI ڈیٹا اینالائز 🤖
    </h1>
    """, unsafe_allow_html=True)

# Sidebar - تصاویر اور آڈیو
with st.sidebar:
    # 1. لوگو
    if os.path.exists("assets/logo.jpg"):
        st.image("assets/logo.jpg", width=200)

    # 2. کارڈ تصویر
    if os.path.exists("my_photo.jpg"):
        st.image("my_photo.jpg", caption="Atta Ur Rehman Khan", use_container_width=True)

    # 3. آڈیو
    audio_path = 'assets/Pakistan_Ka_Saylani___National_Song_Pakistan_2022___Hafiz_Tahir_Qadri___14th_August_Milli_Naghma(128k).mp3'
    if os.path.exists(audio_path):
        st.markdown("### 🎵 Saylani Tarana")
        st.audio(audio_path, format='audio/mp3')

# مین فائل اپلوڈر
uploaded_file = st.file_uploader("CSV فائل اپلوڈ کریں", type=["csv"])

if uploaded_file:
    # صرف پہلی بار فائل اپلوڈ ہونے پر بلون دکھانے کے لیے
    if 'balloons_shown' not in st.session_state:
        st.balloons()
        st.session_state.balloons_shown = True
    
    raw_df = pd.read_csv(uploaded_file)

    # 1. ڈیٹا کلیننگ بٹن
    st.subheader("🧹 ڈیٹا ویو")
    col1, col2 = st.columns(2)
    show_raw = col1.button("Raw Data دیکھیں")
    show_clean = col2.button("Clean Data (Drop NA) دیکھیں")

    display_df = raw_df
    if show_clean:
        display_df = raw_df.dropna()
        st.write("### کلین ڈیٹا (خالی خانے ہٹا دیے گئے)")
    elif show_raw:
        st.write("### اوریجنل ڈیٹا")

    st.dataframe(display_df)

    # 3. ڈیٹا سمری (Summary) - الگ الگ بٹن
    st.subheader("📊 ڈیٹا سمری کنٹرول")
    
    # 3 کالمز بنائیں تاکہ بٹن ایک لائن میں نظر آئیں
    col_s1, col_s2, col_s3 = st.columns(3)
    
    with col_s1:
        if st.button("📊 شماریاتی خلاصہ"):
            st.write("#### شماریاتی خلاصہ (Describe):")
            st.write(display_df.describe())
            
    with col_s2:
        if st.button("🏗️ ڈیٹا سٹرکچر"):
            st.write("#### ڈیٹا کا سٹرکچر (Info):")
            buffer = io.StringIO()
            display_df.info(buf=buffer)
            st.text(buffer.getvalue())
            
    with col_s3:
        if st.button("🧬 ڈیٹا ٹائپس"):
            st.write("#### ڈیٹا ٹائپس:")
            st.write(display_df.dtypes)

    # 2. ویژولائزیشن
    st.subheader("📊 ایڈوانسڈ ویژولیشن")
    plot_type = st.selectbox("پلاٹ کا انتخاب کریں", ["Scatter", "Line", "Bar", "Box", "Violin", "KDE", "Relplot"])
    x_axis = st.selectbox("X-axis", display_df.columns)
    y_axis = st.selectbox("Y-axis", display_df.columns)

    if st.button("Generate Plot"):
        plt.figure(figsize=(10, 5))
        try:
            if plot_type == "Scatter": sns.scatterplot(data=display_df, x=x_axis, y=y_axis)
            elif plot_type == "Line": sns.lineplot(data=display_df, x=x_axis, y=y_axis)
            elif plot_type == "Bar": sns.barplot(data=display_df, x=x_axis, y=y_axis)
            elif plot_type == "Box": sns.boxplot(data=display_df, x=x_axis, y=y_axis)
            elif plot_type == "Violin": sns.violinplot(data=display_df, x=x_axis, y=y_axis)
            elif plot_type == "Relplot": sns.relplot(data=display_df, x=x_axis, y=y_axis)
            elif plot_type == "KDE":
                if pd.api.types.is_numeric_dtype(display_df[x_axis]):
                    sns.kdeplot(data=display_df, x=x_axis)
            st.pyplot(plt)
        except Exception as e:
            st.error(f"ایرر: {e}")

    # 3. AI چیٹ سیکشن
    st.subheader("💬 AI ڈیٹا انالیسز")
    user_question = st.text_input("اپنے ڈیٹا کے بارے میں کوئی بھی سوال پوچھیں:")
    if st.button("Analyze with AI"):
        api_key = os.environ.get("GROQ_API_KEY")
        if api_key:
            client = Groq(api_key=api_key)
            prompt = f"Data columns: {list(display_df.columns)}. User question: {user_question}"
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}], 
                model="llama-3.1-8b-instant"
            )
            st.write(response.choices[0].message.content)
        else:
            st.error("API Key نہیں مل رہی! براہ کرم Streamlit Settings میں Secrets چیک کریں۔")

# 4. Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; font-size: 18px; padding: 20px; line-height: 1.6;">
        🏢 <b>Saylani Mass IT Training (SMIT)</b> <br>
        👨‍🏫 <b>Sir Azeem</b> <br><br>
        <i>"میں آج جو کچھ بھی ہوں، وہ اپنے ادارے اور اپنے استاد کی محنت اور رہنمائی کی بدولت ہوں۔ ہمیں جدید ٹیکنالوجی سکھانے اور اس قابل بنانے کا تہہ دل سے شکریہ۔"</i> 🚀💻
    </div>
    """, unsafe_allow_html=True)