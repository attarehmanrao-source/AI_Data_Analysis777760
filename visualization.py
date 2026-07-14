import streamlit as st
import plotly.express as px
import numpy as np

def show_visualizations(df):
    st.title("📊 Data Visualization")
    
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    category_cols = df.select_dtypes(include="object").columns.tolist()

    chart = st.selectbox("Select Chart", ["Bar Chart", "Line Chart", "Histogram", "Pie Chart", "Scatter Plot"])

    if chart == "Bar Chart" and category_cols and numeric_cols:
        x = st.selectbox("Category", category_cols)
        y = st.selectbox("Value", numeric_cols)
        fig = px.bar(df, x=x, y=y)
        st.plotly_chart(fig)

    elif chart == "Line Chart":
        x = st.selectbox("X Axis", df.columns)
        y = st.selectbox("Y Axis", numeric_cols)
        fig = px.line(df, x=x, y=y)
        st.plotly_chart(fig)

    elif chart == "Histogram":
        col = st.selectbox("Column", numeric_cols)
        fig = px.histogram(df, x=col)
        st.plotly_chart(fig)

    elif chart == "Pie Chart" and category_cols:
        col = st.selectbox("Category", category_cols)
        data = df[col].value_counts()
        fig = px.pie(values=data.values, names=data.index)
        st.plotly_chart(fig)

    elif chart == "Scatter Plot":
        x = st.selectbox("X", numeric_cols)
        y = st.selectbox("Y", numeric_cols)
        fig = px.scatter(df, x=x, y=y)
        st.plotly_chart(fig)