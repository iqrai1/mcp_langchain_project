# server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(a: int, b: int) -> int:
    """Get the weather location"""
    return "its always raining in islamabad"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")