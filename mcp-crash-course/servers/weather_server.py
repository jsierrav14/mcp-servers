from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location"""
    # For demonstration purposes, we'll return a static response.
    # In a real implementation, you would call a weather API here.
    return f"The current weather in {location} is sunny with a temperature of 25°C."
if __name__ == "__main__":
    mcp.run(transport="sse")