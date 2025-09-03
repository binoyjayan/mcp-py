# Weather server

from typing import List
from fastmcp import FastMCP

# from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""
    return f"It's always sunny in {location}."


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="127.0.0.1", port=8080)
