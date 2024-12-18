import sys
import os
from typing import Any, Dict
from dotenv import load_dotenv
from yahooquery import search as yq_search
import yfinance as yf

# Force UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# phi Framework Imports
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools import Tool

# Load environment variables
load_dotenv()

# ----------------------------
# Custom Tools
# ----------------------------

class CustomDuckDuckGo(Tool):
    def __init__(self):
        self.function = {
            "name": "DuckDuckGoTool",
            "description": "Performs a web search using DuckDuckGo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find related news."
                    }
                },
                "required": ["query"]
            }
        }

    def run(self, query: str) -> str:
        # Perform a web search
        return f"Mocked result for query: {query}"


class CustomYFinanceTools(Tool):
    def __init__(self):
        self.function = {
            "name": "YFinanceTool",
            "description": "Fetches stock prices, analyst recommendations, and company info from Yahoo Finance.",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "The stock ticker symbol (e.g., TSLA)."
                    }
                },
                "required": ["symbol"]
            }
        }

    def run(self, symbol: str) -> str:
        # Simulate fetching stock data
        return f"Mocked stock data for symbol: {symbol}"


class TickerLookupTool(Tool):
    def __init__(self):
        self.function = {
            "name": "TickerLookupTool",
            "description": "Searches for the ticker symbol of a given company name using yahooquery.",
            "parameters": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string",
                        "description": "The company name to find the ticker for."
                    }
                },
                "required": ["company_name"]
            }
        }

    def run(self, company_name: str) -> str:
        # Simulate ticker lookup
        return f"Mocked ticker for {company_name}"


# ----------------------------
# Instantiate Tools
# ----------------------------

ticker_lookup_tool = TickerLookupTool()
yfinance_tool = CustomYFinanceTools()
duck_tool = CustomDuckDuckGo()

# ----------------------------
# Agents
# ----------------------------

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[ticker_lookup_tool.function, yfinance_tool.function],
    instructions=[
        "If given a company name (e.g., 'Tesla stocks'), first use TickerLookupTool to find the ticker symbol.",
        "Then use YFinanceTool to fetch stock prices and analyst recommendations.",
        "Display data in a structured table."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Web Agent
web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[duck_tool.function],
    instructions=["Always include sources for any information retrieved."],
    show_tool_calls=True,
    markdown=True
)

# Combined Team of Agents
agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, finance_agent],
    instructions=[
        "Always include reliable sources for news.",
        "For 'Tesla stocks', first find the ticker with TickerLookupTool.",
        "Use YFinanceTool for analyst recommendations.",
        "Use DuckDuckGoTool for latest news.",
        "Use tables for structured data."
    ],
    show_tool_calls=True,
    markdown=True
)

# ----------------------------
# Run the Agent Team
# ----------------------------
if __name__ == "__main__":
    try:
        agent_team.print_response(
            "Summarize analyst recommendations and share the latest news for Tesla stocks.",
            stream=True
        )
    except Exception as e:
        print(f"Error running the agent team: {str(e)}")
