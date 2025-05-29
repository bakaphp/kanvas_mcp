# tools/product_tools.py
from services.events.types import get_types as get_types_tool
from services.events.categories import get_categories as get_categories_tool
from services.events.events import (
    list_events as list_events_tool,
    create_event as create_event_tool,
)


def list_events() -> str:
    return list_events_tool()


def get_types() -> str:
    return get_types_tool()


def get_categories() -> str:
    return get_categories_tool()


def create_event(
    name: str,
    description: str,
    category_id: int,
    type_id: int,
    date: str,
    start_time: str,
    end_time: str,
) -> str:
    return create_event_tool(
        name=name,
        description=description,
        category_id=category_id,
        type_id=type_id,
        date=date,
        start_time=start_time,
        end_time=end_time,
    )
