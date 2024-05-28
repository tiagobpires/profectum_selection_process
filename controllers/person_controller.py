from flask import Blueprint, jsonify, request
from spectree import Response

from dtos.person_dto import PersonDTO, CreatePersonResponseDTO
from factory import api
from services.person_service import (
    create_pipefy_card,
    delete_pipefy_card,
    update_card_to_next_phase,
)
from dtos.default_dto import ErrorResponseDTO, DefaultMessageDTO

person_blueprint = Blueprint("person_controller", __name__, url_prefix="/person")


@person_blueprint.post("/card")
@api.validate(
    json=PersonDTO,
    resp=Response(
        HTTP_201=CreatePersonResponseDTO,
        HTTP_400=ErrorResponseDTO,
        HTTP_500=DefaultMessageDTO,
    ),
    tags=["person"],
)
def create_card():
    """
    Create card
    """
    data = request.json

    response = create_pipefy_card(data)
    card_info = response["data"]["createCard"]["card"]

    return (
        jsonify(
            {
                "message": "Card created.",
                "id": card_info["id"],
                "title": card_info["title"],
            }
        ),
        201,
    )


@person_blueprint.delete("/<card_id>")
@api.validate(
    resp=Response(
        HTTP_200=DefaultMessageDTO,
        HTTP_400=ErrorResponseDTO,
        HTTP_500=DefaultMessageDTO,
    ),
    tags=["person"],
)
def delete_card(card_id: str):
    """
    Delete card
    """
    delete_pipefy_card(card_id)

    return jsonify({"message": "Card deleted."}), 200


@person_blueprint.patch("/<card_id>")
@api.validate(
    resp=Response(
        HTTP_200=DefaultMessageDTO,
        HTTP_400=ErrorResponseDTO,
        HTTP_409=DefaultMessageDTO,
        HTTP_500=DefaultMessageDTO,
    ),
    tags=["person"],
)
def update_card_phase(card_id: str):
    """
    Send card to next phase
    """
    response = update_card_to_next_phase(card_id)

    new_phase = response["data"]["moveCardToPhase"]["card"]["current_phase"]

    return jsonify({"message": f"Card sended to {new_phase}."}), 200
