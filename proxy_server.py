from fastmcp import FastMCP


config = {
    "mcpServers": {
        "kanvas": {  # For single server configs, 'default' is commonly used
            "url": "http://localhost/mcp",
            "transport": "streamable-http"
        }
    }
}

# Create a proxy to the configured server
proxy = FastMCP.as_proxy(config, name="KanvasEventsServer")

# Run the proxy with stdio transport for local access
if __name__ == "__main__":
    proxy.run()
