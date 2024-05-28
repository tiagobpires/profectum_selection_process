from flask import Blueprint, jsonify, request
from spectree import Response

from dtos.city_dto import City, CityResponseDTO
from dtos.default_dto import DefaultMessageDTO, ErrorResponseDTO
from factory import api
from services.city_service import get_city_edges

city_blueprint = Blueprint("city_controller", __name__, url_prefix="/city")


@city_blueprint.get("")
@api.validate(
    resp=Response(
        HTTP_200=CityResponseDTO, HTTP_400=ErrorResponseDTO, HTTP_500=DefaultMessageDTO
    ),
    tags=["city"],
)
def get_city_options():
    """
    Get city options
    """

    city_edges = get_city_edges()

    cities = [
        City(id=city["node"]["id"], title=city["node"]["title"]) for city in city_edges
    ]
    response = CityResponseDTO(cities=cities)

    return jsonify(response.dict()), 200
