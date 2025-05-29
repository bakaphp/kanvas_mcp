# server.py
import inspect
import os
from fastmcp import FastMCP
import mcp_tools.inventory.product_tools as product_tools
import mcp_tools.events.events_tools as events_tool
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("Kanvas MCP")


def initialize_tools():
    # Need to load the tools into the MCP instance
    for name, func in inspect.getmembers(product_tools, inspect.isfunction):
        mcp.add_tool(name, func)
    for name, func in inspect.getmembers(events_tool, inspect.isfunction):
        mcp.add_tool(name, func)


if __name__ == "__main__":
    initialize_tools()
    mcp.run(
        transport="streamable-http",
        host=os.getenv("HOST_URL", "127.0.0.1"),
        port=int(os.getenv("HOST_PORT", 8000)),
        path="/mcp",
    )
