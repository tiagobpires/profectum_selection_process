from config import Config
from error_handlers import GraphQLError, HttpError
from utils import send_pipefy_request


def create_pipefy_card(data: dict) -> dict:
    query = """
    mutation CreateCard($input: CreateCardInput!) {
        createCard(input: $input) {
            card {
                id
                title
            }
        }
    }
    """

    variables = {
        "input": {
            "pipe_id": Config.PIPE_ID,
            "title": data.get("name"),
            "fields_attributes": [
                {"field_id": "nome", "field_value": data.get("name")},
                {
                    "field_id": "data_de_nascimento",
                    "field_value": data.get("birth_date"),
                },
                {"field_id": "cpf", "field_value": data.get("cpf")},
                {"field_id": "telefone", "field_value": data.get("phone")},
                {"field_id": "data", "field_value": data.get("submission_date")},
                {"field_id": "sexo", "field_value": data.get("sex")},
                {"field_id": "hobbies", "field_value": data.get("hobbies")},
                {
                    "field_id": "cidade",
                    "field_value": data.get("city"),
                },
            ],
        }
    }

    response = send_pipefy_request(query, variables)

    if "errors" in response:
        raise GraphQLError(response["errors"])

    return response


def delete_pipefy_card(card_id: str) -> dict:
    query = """
    mutation DeleteCard($input: DeleteCardInput!) {
        deleteCard(input: $input) {
            success
        }
    }
    """

    variables = {"input": {"id": card_id}}

    response = send_pipefy_request(query, variables)

    if "errors" in response:
        raise GraphQLError(response["errors"])

    return response


def update_card_to_next_phase(card_id: str) -> dict:
    phases = [
        {"id": "323403002", "name": "Caixa de entrada"},
        {"id": "323403003", "name": "Fazendo"},
        {"id": "323403004", "name": "Concluído"},
    ]

    current_phase_response = _get_card_current_phase(card_id)

    if "errors" in current_phase_response:
        raise GraphQLError(current_phase_response["errors"])

    current_phase_id = current_phase_response["data"]["card"]["current_phase"]["id"]

    # Determine the next phase
    next_phase_id = None
    for i, phase in enumerate(phases):
        if phase["id"] == current_phase_id and i < len(phases) - 1:
            next_phase_id = phases[i + 1]["id"]
            break

    if not next_phase_id:
        raise HttpError("Card is already in the final phase.", 409)

    response = _move_card_to_next_phase(card_id, next_phase_id)

    if "errors" in response:
        raise GraphQLError(response["errors"])

    return response


def _get_card_current_phase(card_id: str) -> dict:
    query = """
    query GetCardPhase($cardId: ID!) {
        card(id: $cardId) {
            id
            title
            current_phase {
                id
                name
            }
        }
    }
    """

    variables = {"cardId": card_id}

    response = send_pipefy_request(query, variables)
    return response


def _move_card_to_next_phase(card_id: str, next_phase_id: str) -> dict:
    query = """
    mutation MoveCardToPhase($input: MoveCardToPhaseInput!) {
        moveCardToPhase(input: $input) {
            card {
                id
                title
                current_phase {
                    id
                    name
                }
            }
        }
    }
    """

    variables = {"input": {"card_id": card_id, "destination_phase_id": next_phase_id}}

    response = send_pipefy_request(query, variables)
    return response
