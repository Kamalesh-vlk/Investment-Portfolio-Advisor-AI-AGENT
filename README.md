

# 📊 AI-Powered Investment Portfolio Advisor

**💡 Description:**
An AI-powered financial assistant that provides personalized market insights and portfolio recommendations using Cohere LLMs and CrewAI agents.

---

## 📝 Overview

This project leverages **Cohere's LLM** and **CrewAI agents** to deliver actionable investment insights. Users can select a stock exchange, asset types, and risk tolerance, and the AI generates:

1. 📊 A detailed market analysis report
2. 💼 A tailored investment portfolio recommendation

It is designed to help investors make informed decisions based on market trends, risks, and opportunities.

---

## ✨ Features

* 🤖 Multi-agent system: Separate agents for **market analysis** and **portfolio recommendations**
* 📑 Generates **data-backed, structured reports** in Markdown
* 💻 User-friendly **Streamlit interface** for interactive input
* 📱 Responsive single-column layout optimized for all screen sizes
* 💰 Supports multiple asset types: stocks, crypto, mutual funds, ETFs, and bonds

---

## 🛠️ Tech Stack

* 🐍 **Python 3.10+**
* 💻 **Streamlit** for UI
* 🤖 **CrewAI** for agent orchestration
* 🧠 **Cohere API** for large language model processing
* 🔐 **python-decouple** for environment variable management

---

## ⚡ Setup environment variables

Create a `.env` file in the root directory and add your Cohere API key:

```env
COHERE_API_KEY=your_cohere_api_key_here
```

---

## 🚀 Usage

1. Run the Streamlit app:

```bash
streamlit run ipmain.py
```

2. Use the UI to:

* 🌎 Select **Stock Exchange** (India, USA, Global)
* 📦 Choose **Asset Types** (stocks, crypto, ETFs, mutual funds, bonds)
* 🎯 Select **Risk Tolerance** (Low, Moderate, High)

3. Click **Run Advisor** to generate:

* 📊 Market Analysis
* 💼 Portfolio Recommendation

---

## 💡 Sample Input & Output

### 🔹 Sample Input

| Field             | Selected Option |
| ----------------- | --------------- |
| 🌎 Stock Exchange | India           |
| 📦 Asset Types    | Stocks, ETFs    |
| 🎯 Risk Tolerance | Moderate        |

### 🖼️ Sample Output Screenshots

<img width="1366" height="447" alt="Screenshot (19)" src="https://github.com/user-attachments/assets/c0878c53-e7da-4c06-91b0-1008fd0d26e9" />  
<img width="1366" height="581" alt="Screenshot (20)" src="https://github.com/user-attachments/assets/485c34cf-41d0-4a8e-a445-95df25185140" />  
<img width="1366" height="562" alt="Screenshot (22)" src="https://github.com/user-attachments/assets/b4bfeb00-c527-449f-b45c-1ed0e81c1fbd" />  
<img width="1366" height="380" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/7cf41b75-a9bb-43b4-9265-fe17d8fcc8be" />  
<img width="1366" height="411" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/3428a2b8-9c46-4381-81b8-b96ebeb39c23" />  
<img width="1366" height="411" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/55b6d1a5-fea5-4f28-9449-ba3840c28dc5" />  

---

