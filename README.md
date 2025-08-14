

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
![Investment portfolio advisor](https://github.com/user-attachments/assets/78f86f1c-db47-4235-8f4e-6a9249e92843)


---

