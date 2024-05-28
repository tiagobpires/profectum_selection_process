from flask import jsonify
from dtos.default_dto import ErrorResponseDTO, DefaultMessageDTO


class GraphQLError(Exception):
    def __init__(self, errors):
        self.errors = errors


class HttpError(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code


def handle_graphql_error(error):
    response = jsonify(ErrorResponseDTO(errors=error.errors).dict())
    response.status_code = 400
    return response


def handle_http_error(error: HttpError):
    response = jsonify(DefaultMessageDTO(message=error.message).dict())
    response.status_code = error.status_code
    return response


def handle_internal_server_error(error):
    response = jsonify(DefaultMessageDTO(message=str(error)).dict())
    response.status_code = 500
    return response
