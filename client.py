from fastmcp import Client
import asyncio
from fastmcp.client.transports import StreamableHttpTransport
import json

# transport = StreamableHttpTransport(url="http://localhost/mcp")

transport = StreamableHttpTransport(url="http://localhost/mcp")

client = Client(transport)


async def main():
    print("Running client")
    async with client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        result = await client.call_tool("search_products", {"name": "Hello"})
        try:
            raw_text = result[0].text
            parsed_json = json.loads(raw_text)
            print(f"Result: {parsed_json}")
        except TypeError:
            print(f"Result (non-serializable): {result}")


if __name__ == "__main__":
    asyncio.run(main())


# from services.inventory.products import search_products

# if __name__ == "__main__":
#     result = search_products("Ford")
#     print(f"Result: {result}")
