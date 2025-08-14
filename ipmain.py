import os
from crewai import Crew
from decouple import config
from ipagent import InvestmentPortfolioAgents
from iptasks import InvestmentPortfolioTasks
import streamlit as st

# Load Cohere API key
os.environ["COHERE_API_KEY"] = config("COHERE_API_KEY")

class InvestmentPortfolioCrew:
    def __init__(self, stock_exchange, asset_types, risk_tolerance):
        self.stock_exchange = stock_exchange
        self.asset_types = asset_types
        self.risk_tolerance = risk_tolerance

    def run(self):
        agents = InvestmentPortfolioAgents()
        tasks = InvestmentPortfolioTasks()

        agent1 = agents.market_analyzer()
        agent2 = agents.portfolio_recommender()

        task1 = tasks.analyze_market_task(agent1, self.stock_exchange, self.asset_types, self.risk_tolerance)
        task2 = tasks.recommend_portfolio_task(agent2)

        crew = Crew(
            agents=[agent1, agent2],
            tasks=[task1, task2],
            verbose=True,
        )

        return crew.kickoff()

# --- Streamlit UI ---
st.set_page_config(page_title="Investment Portfolio Advisor", page_icon="📊", layout="wide")

# Remove extra spacing on sides
st.markdown("""
<style>
    .css-1d391kg {padding-left: 0rem; padding-right: 0rem;}
    .css-18e3th9 {padding-left: 0rem; padding-right: 0rem;}
</style>
""", unsafe_allow_html=True)

st.title("📊 AI-Powered Investment Portfolio Advisor")
st.write("Get tailored market insights and portfolio recommendations using Cohere & CrewAI.")

# --- Input section ---
stock_exchange = st.selectbox("Choose Stock Exchange:", ["India", "USA", "Global"])
asset_types = st.multiselect(
    "Select Asset Types:",
    ["stocks", "crypto", "mutual funds", "ETFs", "bonds"],
    default=["stocks"]
)
risk_tolerance = st.selectbox("Select Risk Tolerance Level:", ["Low", "Moderate", "High"])

if st.button("Run Advisor"):
    with st.spinner("Analyzing market and preparing recommendations..."):
        crew_runner = InvestmentPortfolioCrew(stock_exchange, ", ".join(asset_types), risk_tolerance)
        result = crew_runner.run()

    st.subheader("💡 Advisor's Output")

    # --- Format output ---
    if isinstance(result, dict):
        market_analysis = result.get("analyze_market_task", "") or result.get("task_1", "")
        portfolio_recommendation = result.get("recommend_portfolio_task", "") or result.get("task_2", "")

        st.markdown("### 📊 Market Analysis")
        st.markdown(market_analysis)

        st.markdown("### 💡 Portfolio Recommendations")
        st.markdown(portfolio_recommendation)

    elif isinstance(result, list):
        if len(result) >= 2:
            st.markdown("### 📊 Market Analysis")
            st.markdown(str(result[0]))

            st.markdown("### 💡 Portfolio Recommendations")
            st.markdown(str(result[1]))
        else:
            st.write(result)
    else:
        try:
            parts = str(result).split("\n\n", 1)
            if len(parts) == 2:
                st.markdown("### 📊 Market Analysis")
                st.markdown(parts[0])
                st.markdown("### 💡 Portfolio Recommendations")
                st.markdown(parts[1])
            else:
                st.markdown(result)
        except Exception:
            st.markdown(result)
