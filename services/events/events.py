import requests
import json
import os
from dotenv import load_dotenv

from util.requests import RequestsUtil

load_dotenv()


def create_event(
    name: str,
    description: str,
    category_id: int,
    type_id: int,
    date: str,
    start_time: str,
    end_time: str,
) -> str:
    graphql_query = """
    mutation CreateEvent(
      $name: String!,
      $description: String!,
      $category_id: ID!,
      $type_id: ID!,
      $date: Date!,
      $start_time: String!,
      $end_time: String!
    ) {
      createEvent(
        input: {
          name: $name,
          description: $description,
          category_id: $category_id,
          type_id: $type_id,
          dates: [
            {
              date: $date,
              start_time: $start_time,
              end_time: $end_time
            }
          ]
        }
      ) {
        id
        name
      }
    }
    """

    payload = {
        "query": graphql_query,
        "variables": {
            "name": name,
            "description": description,
            "category_id": category_id,
            "type_id": type_id,
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
        },
    }

    response = RequestsUtil.post(payload=payload)
    data = response.json()
    return json.dumps(
        data
    )


def list_events() -> str:
    print("Listing all events")
    graphql_query = """
    query Events {
      events {
        data {
          id
          name
          type {
            name
          }
          eventStatus {
            id
            name
          }
          versions {
            data {
              id
              name
              agenda
              description
              slug
              dates {
                id
                date
                start_time
                end_time
              }
            }
          }
        }
      }
    }
    """

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('KANVAS_AUTH_TOKEN')}",
        "X-Kanvas-App": os.getenv("KANVAS_APP_ID"),
        "X-Kanvas-Location": os.getenv("KANVAS_LOCATION"),  # Still valid if needed
    }

    payload = {
        "query": graphql_query,
    }

    response = requests.post(os.getenv("KANVAS_API_URL"), json=payload, headers=headers)

    data = response.json()
    return json.dumps(
        {"events": data.get("data", {}).get("events", {}).get("data", [])}
    )


def list_reminders() -> str:
    print("Listing all reminders")
    graphql_query = """
    query {
      reminders {
        data {
          id
          name
          description
        }
      }
    }
    """

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('KANVAS_AUTH_TOKEN')}",
        "X-Kanvas-App": os.getenv("KANVAS_APP_ID"),
        "X-Kanvas-Location": os.getenv("KANVAS_LOCATION"),  # Still valid if needed
    }

    payload = {
        "query": graphql_query,
    }

    response = requests.post(os.getenv("KANVAS_API_URL"), json=payload, headers=headers)

    data = response.json()
    return json.dumps(
        {"reminders": data.get("data", {}).get("reminders", {}).get("data", [])}
    )
