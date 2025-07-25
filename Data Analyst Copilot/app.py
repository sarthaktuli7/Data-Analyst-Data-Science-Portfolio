# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai
import io
import ydata_profiling
from streamlit_chat import message
from utils import openai_utils, eda_utils, viz_utils
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Streamlit page config
st.set_page_config(page_title="📊 Data Analyst Copilot", layout="wide")
st.title("📊 Data Analyst Copilot")

# ✅ File uploader
uploaded_file = st.file_uploader("📁 Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head())

    # ✅ Auto Profiling Report
    st.subheader("📈 Auto Profiling Report")
    if st.checkbox("✅ Generate Full Profile Report"):
        profile = df.profile_report(title="Pandas Profiling Report")
        profile.to_file("report.html")
        with open("report.html", 'r', encoding='utf-8') as file:
            html = file.read()
            st.components.v1.html(html, height=800, scrolling=True)

    # ✅ Basic EDA Summary
    st.subheader("📋 Basic EDA Summary")
    st.write("**🔢 Shape:**", df.shape)
    st.write("**📊 Column Types:**", df.dtypes)
    st.write("**❓ Missing Values:**", df.isnull().sum())
    st.write("**📉 Descriptive Statistics:**")
    st.write(df.describe())

    # ✅ GPT Summary
    if st.button("🧠 Run AI Insight Engine"):
        st.subheader("🤖 GPT Summary")
        sample_data = df.head(10).to_csv(index=False)
        with st.spinner("🔍 Analyzing with GPT..."):
            try:
                gpt_output = openai_utils.generate_gpt_summary(sample_data)
            except Exception as e:
                gpt_output = "⚠️ GPT failed, retrying..."
                try:
                    gpt_output = openai_utils.generate_gpt_summary(sample_data)
                except:
                    gpt_output = f"❌ Second attempt failed. Error: {e}"
        st.markdown(gpt_output)

    # ✅ Quick Visualizations
    st.subheader("📊 Quick Visualizations")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_cols) >= 2:
        x_axis = st.selectbox("📌 Select X-Axis", numeric_cols)
        y_axis = st.selectbox("📌 Select Y-Axis", numeric_cols, index=1)

        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("⚠️ Not enough numeric columns for charting.")

    # ✅ GPT Column Insight
    st.subheader("📌 GPT Insight for Specific Column")
    selected_column = st.selectbox("🧾 Select a column", df.columns)
    if st.button("💡 Generate Insight for Column"):
        column_prompt = f"Analyze the column '{selected_column}' in this dataset. Look for patterns, distributions, and anomalies."
        column_sample = df[selected_column].head(50).to_csv(index=False)
        full_prompt = column_prompt + "\n\nData Preview:\n" + column_sample
        column_output = openai_utils.call_gpt(full_prompt)
        st.markdown(column_output)

    # ✅ Outlier Detection
    st.subheader("📉 Outlier Detection")
    outlier_column = st.selectbox("📍 Select numeric column", numeric_cols)
    if st.button("🔎 Detect Outliers"):
        fig = viz_utils.plot_outliers(df, outlier_column)
        st.pyplot(fig)

    # ✅ Ask the Data (Chatbot)
    st.subheader("💬 Ask the Data (Chatbot)")
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    query = st.text_input("💬 Ask your question about the dataset")
    if st.button("Submit Question") and query:
        question_prompt = f"You are a data analyst. Given this dataset preview:\n{df.head().to_csv(index=False)}\n\nAnswer the question: {query}"
        reply = openai_utils.call_gpt(question_prompt)
        st.session_state.messages.append(("You", query))
        st.session_state.messages.append(("Copilot", reply))

    for sender, msg in st.session_state.messages:
        message(msg, is_user=(sender == "You"))

    # ✅ Download summary
    st.subheader("📥 Download AI Summary")
    if st.button("📄 Download Summary as TXT"):
        download_text = io.StringIO()
        download_text.write(gpt_output)
        download_text.seek(0)
        st.download_button(
            label="📄 Download Summary",
            data=download_text,
            file_name="gpt_insights.txt",
            mime="text/plain"
        )
