import json
import os
from dotenv import load_dotenv

from util.requests import RequestsUtil

load_dotenv()


def get_categories() -> str:
    graphql_query = """
    query EventCategories {
        eventCategories(first: 10) {
            data {
                id
                name
            }
        }
    }
    """

    payload = {
        "query": graphql_query,
        # "variables": {"name": name}
    }

    response = RequestsUtil.post(payload)
    data = response.json()

    return json.dumps(
        {"categories": data.get("data", {}).get("eventCategories", {}).get("data", [])}
    )
