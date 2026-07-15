import os
from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables
load_dotenv()

# Create Tavily client
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def search_web(query: str) -> str:
    """
    Searches the web using Tavily
    and returns the search results.
    """

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    return response