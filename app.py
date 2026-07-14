import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# پیج کی سیٹنگز
st.set_page_config(page_title="AI Data Analysis Tool", layout="wide")

# آپ کی تصویر شامل کرنا
try:
    st.image("my_photo.jpg", width=150)
except:
    st.warning("Image file 'my_photo.jpg' not found in project folder.")

st.title("AI Data Analysis Tool")
st.write("Welcome to your advanced data analysis dashboard.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # ڈیٹا کی بنیادی معلومات
    st.write("### Data Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Rows", df.shape[0])
    col2.metric("Total Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())
    
    st.write("#### Data Preview")
    st.dataframe(df.head())

    # ڈیٹا کلیننگ
    if st.checkbox("Clean Data (Drop missing values)"):
        df = df.dropna()
        st.write("Missing values removed!")
        st.dataframe(df.head())

    # وزولائزیشن
    st.write("### Data Visualization")
    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)
    
    if st.button("Generate Chart"):
        fig, ax = plt.subplots()
        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)
        st.success("Chart generated successfully!")
else:
    st.info("Please upload a CSV file to get started.")