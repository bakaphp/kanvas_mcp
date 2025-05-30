from typing import Annotated
from pydantic import Field
from services.events.types import get_types as get_types_tool
from services.events.categories import get_categories as get_categories_tool
from services.events.events import (
    list_events as list_events_tool,
    create_event as create_event_servive,
)


def list_events() -> str:
    return list_events_tool()


def get_types() -> str:
    '''
    Get the list of the different types of events one can schudule/.
    '''
    return get_types_tool()


def get_categories() -> str:
    '''
    Get a list of the available categories for events.
    '''
    return get_categories_tool()


def create_event(
    name: Annotated[str, Field(description="Name of the event.")],
    description: Annotated[str, Field(description="Description of the event.")],
    category_id: Annotated[int, Field(description="The even category id.")],
    type_id: Annotated[int, Field(description="The event type id.")],
    date: Annotated[
        str,
        Field(description="This is the date of the event. Something like 2024-01-01."),
    ],
    start_time: Annotated[
        str,
        Field(
            description="The starting time of the event.In the format of for example 00:00."
        ),
    ],
    end_time: Annotated[
        str,
        Field(
            description="The ending time of the event.In the format of for example 00:00."
        ),
    ],
) -> str:
    '''
    Creates an event from the information given.
    '''
    return create_event_servive(
        name=name,
        description=description,
        category_id=category_id,
        type_id=type_id,
        date=date,
        start_time=start_time,
        end_time=end_time,
    )
