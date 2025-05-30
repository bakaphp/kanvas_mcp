from email import header
from h11 import Request
import requests
import json
import os
from util.requests import RequestsUtil
from dotenv import load_dotenv

load_dotenv()


def get_types() -> str:
    graphql_query = """
    query EventCategories {
        eventTypes(first: 10) {
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

    # You could return filtered data, or raw depending on your needs:
    return json.dumps(
        {"types": data.get("data", {}).get("eventTypes", {}).get("data", [])}
    )
