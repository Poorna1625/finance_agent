Finance & News Agent Team

A Python project leveraging the phi framework and advanced language models to create AI-powered agents for real-time financial data retrieval and news aggregation. This project demonstrates how specialized agents can collaborate to answer complex queries, combining financial insights and the latest news into a cohesive, user-friendly response.

Features

Web Agent:

Fetches the latest news using DuckDuckGo.

Includes reliable sources for every piece of information retrieved.

Outputs results in Markdown format for easy readability.

Finance Agent:

Retrieves real-time stock prices, analyst recommendations, and company information using Yahoo Finance tools.

Displays financial data in clear, easy-to-read tables.

Combined Agent Team:

Collaborates to handle multi-domain queries.

Aggregates responses from both agents to provide comprehensive answers.

Technologies Used

Language Model: Groq llama-3.3-70b-versatile.

phi Framework: Powers the agents and their workflows.

Third-Party Libraries:

yfinance: For financial data retrieval.

dotenv: For secure environment variable management.

yahooquery: For extended financial data features.

Setup Instructions

1. Clone the Repository
2.  Install Dependencies
3.  Set Up Environment Variables
4.  Run the Script

   The agents respond to complex queries like: Summarize analyst recommendations and share the latest news for AAPL and GOOGL stock for last week.
   
