import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from groq import Groq

# Page Config
st.set_page_config(layout="wide")
st.title("🎓 Saylani Mass IT Training - AI Data Analysis")

# Sidebar
if os.path.exists("my_photo.jpg"):
    st.sidebar.image("my_photo.jpg", caption="Atta Ur Rehman Khan", use_column_width=True)

uploaded_file = st.file_uploader("CSV فائل اپلوڈ کریں", type=["csv"])

if uploaded_file:
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

    # 2. ایڈوانسڈ ویژولائزیشن
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
                else:
                    st.error("⚠️ KDE پلاٹ صرف نمرک (Numeric) ڈیٹا پر کام کرتا ہے۔")
            st.pyplot(plt)
        except Exception as e:
            st.error(f"ایرر: {e}")

    # 3. AI چیٹ سیکشن (یہ پہلے غائب تھا)
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

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; font-size: 18px; padding: 20px; line-height: 1.6;">
        🏢 <b>Saylani Mass IT Training (SMIT)</b> <br>
        👨‍🏫 <b>Sir Azeem</b> <br><br>
        <i>"میں آج جو کچھ بھی ہوں، وہ اپنے ادارے اور اپنے استاد کی محنت اور رہنمائی کی بدولت ہوں۔ ہمیں جدید ٹیکنالوجی سکھانے اور اس قابل بنانے کا تہہ دل سے شکریہ۔"</i> 🚀💻
    </div>
    """, unsafe_allow_html=True)