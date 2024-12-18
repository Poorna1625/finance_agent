# Standard Libraries
import os

# Third-Party Libraries
import yfinance as yf
from dotenv import load_dotenv

# phi Framework Imports
from phi.agent import Agent  
from phi.model.groq import Groq  
from phi.tools.duckduckgo import DuckDuckGo  
from phi.tools.yfinance import YFinanceTools  

# Load environment variables explicitly
load_dotenv()

# Web Agent: Fetches latest news using DuckDuckGo
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources for any information retrieved."],
    show_tool_calls=True,
    markdown=True
)

# Finance Agent: Fetches stock prices, analyst recommendations, and company info
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Fetch stock prices and analyst recommendations in table format."],
    show_tool_calls=True,
    markdown=True,
)

# Combined Team of Agents
agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, finance_agent],
    instructions=[
        "Always include reliable sources for news.",
        "Use tables to display financial data and make comparisons clear."
    ],
    show_tool_calls=True,
    markdown=True
)

# Test the Agent Team
if __name__ == "__main__":
    agent_team.print_response(
        "Summarize analyst recommendations and share the latest news for AAPL and GOOGL stock for last week.",
        stream=True
    )
