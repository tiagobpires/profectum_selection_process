from flask import Flask
from spectree import SpecTree
from validate_docbr import CPF

from config import Config
from error_handlers import (
    GraphQLError,
    handle_graphql_error,
    handle_internal_server_error,
)

api = SpecTree(
    "flask",
    mode="strict",
    title="Desafio Profectum API",
    version="v.1.0",
    path="docs",
)
cpf = CPF()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from controllers import person_blueprint, city_blueprint

    app.register_blueprint(person_blueprint)
    app.register_blueprint(city_blueprint)

    app.register_error_handler(GraphQLError, handle_graphql_error)
    app.register_error_handler(Exception, handle_internal_server_error)

    api.register(app)  # URL: http://localhost:5000/docs/swagger

    return app
