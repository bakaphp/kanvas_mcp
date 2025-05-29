import requests
import os


class RequestsUtil(object):
    """
    Utility class for making HTTP requests.
    """

    @staticmethod
    def post(payload: dict, headers: dict) -> requests.Response:
        """
        Make a POST request.
        """
        if headers is None:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {os.getenv('KANVAS_AUTH_TOKEN')}",
                "X-Kanvas-App": os.getenv("KANVAS_APP_ID"),
                # "X-Kanvas-Location": os.getenv("KANVAS_LOCATION"),
            }

        return requests.post(os.getenv("KANVAS_API_URL"), json=payload, headers=headers)
