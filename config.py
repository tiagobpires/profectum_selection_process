import os
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    PIPEFY_TOKEN = os.environ.get("PIPEFY_TOKEN")
    PIPE_ID = os.environ.get("PIPE_ID")
    PIPEFY_URL = "https://api.pipefy.com/graphql"

    APP_TITLE = "Desafio Profectum API"

    @staticmethod
    def init_app(app):
        pass
