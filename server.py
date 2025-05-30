# server.py
import inspect
import os
from fastmcp import FastMCP
import mcp_tools.inventory.product_tools as product_tools
from mcp_tools.events.events_tools import (
    create_event,
    get_categories,
    get_types
)
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("Kanvas MCP")


def initialize_tools():
    # Need to load the tools into the MCP instance
    # for name, func in inspect.getmembers(product_tools, inspect.isfunction):
    #     # mcp.remove_tool(name)
    #     mcp.add_tool(func)
    # for name, func in inspect.getmembers(events_tool, inspect.isfunction):
        # mcp.remove_tool(name)
    mcp.add_tool(create_event,'create_event')
    mcp.add_tool(get_categories,'get_categories')
    mcp.add_tool(get_types,'get_types')


if __name__ == "__main__":
    initialize_tools()
    mcp.run(
        transport="streamable-http",
        host=os.getenv("HOST_URL", "127.0.0.1"),
        port=int(os.getenv("HOST_PORT", 8000)),
        path="/mcp",
    )
