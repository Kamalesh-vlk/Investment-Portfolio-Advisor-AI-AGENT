from crewai import Agent
from langchain_cohere import ChatCohere
from decouple import config

class InvestmentPortfolioAgents:
    def __init__(self):
        self.llm = ChatCohere(cohere_api_key=config("COHERE_API_KEY"), model="command-r")

    def market_analyzer(self):
        return Agent(
            role="Market Analyzer",
            goal=(
                "Analyze the selected stock exchange market, asset types, "
                "and assess opportunities based on the given risk tolerance."
            ),
            backstory=(
                "You are a highly experienced financial market analyst. "
                "You provide detailed market insights, trends, and factors affecting asset classes."
            ),
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )

    def portfolio_recommender(self):
        return Agent(
            role="Portfolio Recommender",
            goal="Create a tailored investment portfolio plan based on market analysis.",
            backstory=(
                "You are a skilled portfolio manager who balances risk and return. "
                "You use the latest market analysis to create actionable recommendations."
            ),
            allow_delegation=False,
            verbose=True,
            llm=self.llm
        )
