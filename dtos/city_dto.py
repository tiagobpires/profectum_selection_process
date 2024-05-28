from pydantic.v1 import BaseModel


class City(BaseModel):
    id: str
    title: str


class CityResponseDTO(BaseModel):
    cities: list[City]
