import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Page Config
st.set_page_config(layout="wide")
st.title("🎓 Saylani Mass IT Training - AI Data Analysis")

# Sidebar
if os.path.exists("my_photo.jpg"):
    st.sidebar.image("my_photo.jpg", caption="Atta Ur Rehman Khan", use_column_width=True)

uploaded_file = st.file_uploader("CSV فائل اپلوڈ کریں", type=["csv"])

if uploaded_file:
    raw_df = pd.read_csv(uploaded_file)
    
    # ڈیٹا کلیننگ بٹن
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

    # پلاٹ سیکشن
    st.subheader("📊 ایڈوانسڈ ویژولائزیشن")
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

# بہتر کیا گیا فوٹر
st.markdown("---")
st.markdown("""
    <div style="text-align: center; font-size: 18px; padding: 20px; line-height: 1.6;">
        🏢 <b>Saylani Mass IT Training (SMIT)</b> <br>
        👨‍🏫 <b>Sir Azeem</b> <br><br>
        <i>"میں آج جو کچھ بھی ہوں، وہ اپنے ادارے اور اپنے استاد کی محنت اور رہنمائی کی بدولت ہوں۔ ہمیں جدید ٹیکنالوجی سکھانے اور اس قابل بنانے کا تہہ دل سے شکریہ۔"</i> 🚀💻
    </div>
    """, unsafe_allow_html=True)