from crewai import Task

class InvestmentPortfolioTasks:
    def analyze_market_task(self, agent, stock_exchange, asset_types, risk_tolerance):
        return Task(
            description=(
                f"You are a senior financial market strategist specializing in {stock_exchange}. "
                f"Provide a detailed analysis of the {asset_types} market conditions for a {risk_tolerance} risk tolerance investor. "
                "The report must be well-structured in Markdown and include:\n"
                "1. **Title** summarizing current market outlook.\n"
                "2. **Executive Summary** (3–5 sentences overview).\n"
                "3. **Current Market Trends** — covering macroeconomic factors, sector performance, and investor sentiment.\n"
                "4. **Opportunities** — promising sectors or assets and why they are attractive now.\n"
                "5. **Risks & Challenges** — possible economic, policy, or market risks.\n"
                "6. **Key Data Points** — market indices, inflation, interest rates, sector returns.\n"
                "7. **Conclusion** — short summary for the investor profile.\n"
                "Ensure output is detailed (minimum 500 words), data-backed, and formatted with headings, bullet points, and bold keywords."
            ),
            agent=agent,
            expected_output="A comprehensive, multi-section market analysis in Markdown."
        )


    def recommend_portfolio_task(self, agent):
        return Task(
            description=(
                "Based on the market analysis, create an **optimal investment portfolio recommendation**. "
                "Include:\n"
                "1. Asset allocation percentages.\n"
                "2. Suggested companies/assets.\n"
                "3. Expected returns and potential risks.\n"
                "4. Justification for each recommendation.\n"
                "Format it in Markdown with headings and bullet points."
            ),
            agent=agent,
            expected_output="A portfolio recommendation report in Markdown."
        )
