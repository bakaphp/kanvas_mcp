import os
import asyncio
from fastmcp import FastMCP, Context
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware


load_dotenv()

# --- Initialize FastMCP Server Instance ---
# The DeprecationWarning you see is about passing transport-specific settings
# to the FastMCP constructor. Your current initialization is fine here.
mcp = FastMCP("Kanvas MCP", description="Provides tools for event management.")


# --- Define custom MCP tools ---
@mcp.tool()
async def create_event(
    event_name: str,
    event_type: str,
    category: str,
    date: str,
    time: str,
    location: str,
    ctx: Context,
) -> str:
    """Creates a new event with the specified details.

    Args:
        event_name (str): The name of the event.
        event_type (str): The type of the event (e.g., 'concert', 'workshop').
        category (str): The category of the event (e.g., 'music', 'education').
        date (str): The date of the event (YYYY-MM-DD format).
        time (str): The time of the event (HH:MM format).
        location (str): The location where the event will take place.
        ctx (Context): The MCP context for sending feedback.

    Returns:
        str: A confirmation message or an error.
    """
    await ctx.info(f"Attempting to create event: {event_name}")
    print(
        f"DEBUG: Creating Event: {event_name}, Type: {event_type}, Category: {category}, Date: {date}, Time: {time}, Location: {location}"
    )
    await asyncio.sleep(0.5)
    return f"Event '{event_name}' of type '{event_type}' in category '{category}' at {location} on {date} {time} has been successfully created!"


@mcp.tool()
async def get_categories(ctx: Context) -> list[str]:
    """Retrieves a list of available event categories.

    Args:
        ctx (Context): The MCP context.

    Returns:
        list[str]: A list of event categories.
    """
    await ctx.info("Retrieving event categories...")
    print("DEBUG: Getting event categories")
    await asyncio.sleep(0.2)  # Simulate some processing time
    return ["Music", "Sports", "Education", "Art", "Community"]


@mcp.tool()
async def get_types(ctx: Context) -> list[str]:
    """Retrieves a list of available event types.

    Args:
        ctx (Context): The MCP context.

    Returns:
        list[str]: A list of event types.
    """
    await ctx.info("Retrieving event types...")
    print("DEBUG: Getting event types")
    await asyncio.sleep(0.2)  # Simulate some processing time
    return ["Concert", "Workshop", "Seminar", "Exhibition", "Festival", "Meetup"]


# --- Run the FastMCP server ---
if __name__ == "__main__":
    HOST_URL = os.getenv("HOST_URL", "0.0.0.0")
    HOST_PORT = int(os.getenv("HOST_PORT", 8001))
    MCP_PATH = "/mcp"  # FastMCP will serve its endpoints under this base path
    ADK_WEB_UI_URL = os.getenv("ADK_WEB_UI_URL", "http://localhost:8000")
    cors_origins_list = [
        ADK_WEB_UI_URL,
        "http://localhost",
        "http://127.0.0.1",
        "http://0.0.0.0",
        "*",
    ]

    # Attempt to add CORS middleware directly to the underlying ASGI app

    if hasattr(mcp, "app") and mcp.app is not None:
        mcp.app.add_middleware(
            CORSMiddleware,
            allow_origins=cors_origins_list,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        print(
            f"CORS middleware successfully configured for origins: {cors_origins_list}"
        )
    else:
        print(
            "Warning: Could not access `mcp.app` to apply CORS middleware directly. "
            "CORS might not be configured as expected. Check FastMCP documentation for your version."
        )

    print(
        f"Starting Kanvas Custom MCP Server at http://{HOST_URL}:{HOST_PORT}{MCP_PATH}"
    )
    print(
        f"Ensure the ADK_BACKEND_URL environment variable in your ADK project is set to this URL."
    )

    mcp.run(
        transport="streamable-http",
        host=HOST_URL,
        port=HOST_PORT,
        path=MCP_PATH,
        log_level="debug",
    )
