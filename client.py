from fastmcp import Client
import asyncio
from fastmcp.client.transports import StreamableHttpTransport
import json
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


transport = StreamableHttpTransport(url="http://localhost/mcp")

# transport = StreamableHttpTransport(url="http://0.0.0.0:8888/mcp")

client = Client(transport)


async def get_categories():
    logger.info("Getting categories")
    async with client:
        result = await client.call_tool("get_categories", {})
        try:
            raw_text = result[0].text
            parsed_json = json.loads(raw_text)
            logger.info(f"Categories result: {parsed_json}")
            return parsed_json
        except TypeError:
            logger.error(f"Categories non-serializable result: {result}")
            return None


async def get_types():
    logger.info("Getting types")
    async with client:
        result = await client.call_tool("get_types", {})
        try:
            raw_text = result[0].text
            parsed_json = json.loads(raw_text)
            logger.info(f"Types result: {parsed_json}")
            return parsed_json
        except TypeError:
            logger.error(f"Types non-serializable result: {result}")
            return None


async def create_event(
    name: str,
    description: str,
    category_id: int,
    type_id: int,
    date: str,
    start_time: str,
    end_time: str,
):
    logger.info("Creating event")
    async with client:
        result = await client.call_tool(
            "create_event",
            {
            "name": name,
            "description": description,
            "category_id": category_id,
            "type_id": type_id,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            },
        )
        try:
            raw_text = result[0].text
            logger.info(f"Raw response: {raw_text}")
            # parsed_json = json.loads(raw_text)
            # logger.info(f"Event creation result: {parsed_json}")
        except Exception as e:
            # We’re *inside* create_event but the call blew up.
            logger.error("create_event call_tool failed: %s", e, exc_info=True)

            # If the transport captured a raw body you can sometimes get it like this:
            if hasattr(e, "response") and e.response is not None:
                logger.error("Raw body >>> %r", e.response.text)
            raise  # re-raise so the caller still sees the failure


async def main():
    category = await get_categories()
    logger.info(f"Category: {category['categories'][0]['id']}")
    event_type = await get_types()
    logger.info(f"Type: {event_type['types'][0]['id']}")
    await create_event(
        name="Example2",
        description="Example description",
        category_id=6,
        type_id=12,
        date="2024-01-01",
        start_time="09:00",
        end_time="10:00",
    )


if __name__ == "__main__":
    asyncio.run(main())


# # from services.events.types import get_types
# from services.events.events import create_event

# if __name__ == "__main__":
#     result = create_event(name="Example2",
#         description="Example description",
#         category_id=6,
#         type_id=12,
#         date="2024-01-01",
#         start_time="09:00",
#         end_time="10:00",
#     )
#     print(f"Result: {result}")
