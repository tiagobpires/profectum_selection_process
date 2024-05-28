import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.pipefy.com/graphql"
headers = {
    "Authorization": "Bearer %s" % os.environ.get("PIPEFY_TOKEN"),
    "Content-Type": "application/json",
}
pipe_id = os.environ.get("PIPE_ID")


def get_start_form_fields():
    query = (
        """
    {
        pipe(id: %s) {
            id
            name
            phases {
                id
                name
            }
            start_form_fields {
                id
                label
                type
                required
                options 
            }
        }
    }
    """
        % pipe_id
    )

    response = requests.post(
        url,
        json={"query": query},
        headers=headers,
    )

    return response.json()


def get_phases_and_cards():
    query = """
    query GetPipePhasesAndCards($pipeId: ID!) {
        pipe(id: $pipeId) {
            id
            phases {
                id
                name
                cards {
                    edges {
                        node {
                            id
                            title
                        }
                    }
                }
            }
        }
    }
    """
    response = requests.post(
        url,
        json={"query": query, "variables": {"pipeId": pipe_id}},
        headers=headers,
    )

    return response.json()


if __name__ == "__main__":

    start_form_fields = get_start_form_fields()
    pretty_json = json.dumps(start_form_fields, indent=4, ensure_ascii=False)
    print(pretty_json)

    print("-----------------")

    phases_and_cards = get_phases_and_cards()
    pretty_json = json.dumps(phases_and_cards, indent=4, ensure_ascii=False)
    print(pretty_json)
