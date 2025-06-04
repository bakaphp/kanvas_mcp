from email import header
import requests
import json
import os
from dotenv import load_dotenv
from util.requests import RequestsUtil

load_dotenv()


def search_products(name: str) -> str:
    print(f"Searching for products with name: {name}")
    graphql_query = """
    query {
      products(
      orderBy: [
            {
                column: ID,
                order: DESC
            }
        ]
      first: 2
    ) {
        data {
            id
            name
            description
        }
      }
    }
    """

    payload = {
        "query": graphql_query,
        # "variables": {"name": name}
    }

    response = RequestsUtil.post(payload)
    data = response.text

    print(f"{data}")
    exit()

    return json.dumps({"products": data})
