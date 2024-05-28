from error_handlers import GraphQLError
from utils import send_pipefy_request


def get_city_edges() -> list:
    query = """
    query GetCityOptions($table_id: ID!) {
        table_records(table_id: $table_id) {
            edges {
                node {
                    id
                    title
                }
            }
        }
    }
    """

    variables = {"table_id": 303843634}

    response = send_pipefy_request(query, variables)

    if "errors" in response:
        raise GraphQLError(response["errors"])

    return response["data"]["table_records"]["edges"]
