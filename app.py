import streamlit as st
import pandas as pd
from google import genai
import matplotlib.pyplot as plt

# Streamlit secrets se API Key hasil karna (Yeh GitHub par safe rahega)
try:
    api_key = st.secrets["API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error("API Key nahi mili. Bara-e-meharbani Streamlit Settings mein 'Secrets' set karein.")

st.title("AI Data Analyst Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # CSV file ko load karna
    df = pd.read_csv(uploaded_file, encoding='utf-8')
    
    st.write("### Data Preview:")
    st.write(df.head())
    
    # Simple Analysis: Total Sales
    st.write("### Analysis Results:")
    if 'Sales' in df.columns:
        total_sales = df['Sales'].sum()
        st.metric(label="Total Sales", value=f"{total_sales:,}")
        
        # Chart dikhane ke liye (Category wise)
        if 'Category' in df.columns:
            st.write("### Sales by Category:")
            sales_by_cat = df.groupby('Category')['Sales'].sum()
            st.bar_chart(sales_by_cat)
    else:
        st.warning("CSV file mein 'Sales' ya 'Category' ka column nahi mila.")

    st.write("Data Analysis mukammal ho gaya!")