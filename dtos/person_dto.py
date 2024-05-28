from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic.v1 import BaseModel, Field, validator

from factory import cpf


class SexEnum(str, Enum):
    male = "Masculino"
    female = "Feminino"
    prefer_not_to_answer = "Prefere não responder"


class HobbyEnum(str, Enum):
    theater = "Teatro"
    music = "Música"
    cinema = "Cinema"
    sports = "Esportes"
    reading = "Leitura"
    travel = "Viagem"
    arts = "Artes"


class PersonDTO(BaseModel):
    name: str = Field(..., example="João Silva", max_length=255)
    birth_date: Optional[date] = Field(None, example="22/10/2001")
    cpf: Optional[str] = Field(None, example="809.480.140-91")
    phone: Optional[str] = Field(None, example="11999887766")
    submission_date: Optional[datetime] = Field(None, example="22/07/2022 14:48:00")
    sex: Optional[SexEnum] = Field(None, example="Masculino")
    hobbies: Optional[list[HobbyEnum]] = Field(None, example=["Cinema", "Leitura"])
    city: list[str] = Field(
        ..., example=["850256930"], description="city node ID from table"
    )

    @validator("cpf")
    def validate_cpf(cls, value):
        if value and not cpf.validate(value):
            raise ValueError("Invalid CPF format")
        return value

    @validator("birth_date", pre=True)
    def validate_birth_date(cls, v):
        try:
            return datetime.strptime(v, "%d/%m/%Y")
        except ValueError:
            raise ValueError("birth_date must be in the format 'DD/MM/YYYY'")

    @validator("submission_date", pre=True)
    def validate_submission_date(cls, v):
        try:
            return datetime.strptime(v, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            raise ValueError(
                "submission_date must be in the format 'DD/MM/YYYY HH:MM:SS'"
            )


class CreatePersonResponseDTO(BaseModel):
    message: str
    id: int
    title: str
