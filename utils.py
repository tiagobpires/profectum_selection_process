import requests
from config import Config


def send_pipefy_request(query: str, variables: dict) -> dict:
    headers = {
        "Authorization": f"Bearer {Config.PIPEFY_TOKEN}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        Config.PIPEFY_URL,
        json={"query": query, "variables": variables},
        headers=headers,
    )

    return response.json()
