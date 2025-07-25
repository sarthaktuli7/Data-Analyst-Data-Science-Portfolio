# 📊 Data Analyst Copilot

[![Streamlit App](https://img.shields.io/badge/Launch%20App-Streamlit-blue?logo=streamlit)](https://data-analyst-copilot.streamlit.app/)

**Data Analyst Copilot** is an AI-powered web app built using **Streamlit** and **OpenAI** APIs to assist data analysts in exploratory data analysis, summarization, and quick insights — all in an intuitive interface.

---

## 🚀 Live Demo
👉 **Try the app:** [https://data-analyst-copilot.streamlit.app](https://data-analyst-copilot.streamlit.app)

---

## ⚙️ Features

- 🔍 **Ask Questions**: Ask natural language queries about your dataset (e.g., “Which column has the most missing values?”).
- 📊 **Auto EDA**: Generates interactive profiling reports using `ydata-profiling`.
- 📁 **Upload CSVs**: Upload your own datasets securely.
- 💬 **Chat with Data**: Uses OpenAI to explain, summarize, and explore your dataset.
- ☁️ **Streamlit Cloud Hosted**: No local setup needed — runs entirely in the browser.

---

## 🧰 Tech Stack

- 🐍 Python 3.11+
- 🧠 OpenAI API
- 🌐 Streamlit
- 📊 ydata-profiling
- ☁️ Deployed via Streamlit Cloud

---

## 🛠️ Setup Locally

```bash
git clone https://github.com/sarthaktuli7/Data-Analyst-Data-Science-Portfolio.git
cd "Data Analyst Copilot"
pip install -r requirements.txt
streamlit run app.py
Create a .env file

ini
Copy
Edit
OPENAI_API_KEY=your_openai_key_here
📦 Folder Structure
bash
Copy
Edit
Data Analyst Copilot/
│
├── app.py                  # Main Streamlit App
├── helpers.py              # Helper functions
├── utils/                  # Utilities (file handling, prompts)
├── .env                    # Secret API key (ignored in Git)
└── requirements.txt        # Python dependencies

👨‍💻 Author
Made with ❤️ by Sarthak Tuli
