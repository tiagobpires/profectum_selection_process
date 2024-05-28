from typing import Optional

from pydantic.v1 import BaseModel


class ErrorLocation(BaseModel):
    column: int
    line: int


class ErrorExtensions(BaseModel):
    code: str
    correlation_id: Optional[str] = None


class ErrorDetail(BaseModel):
    message: str
    locations: Optional[list[ErrorLocation]] = None
    path: Optional[list[str]] = None
    extensions: Optional[ErrorExtensions] = None


class ErrorResponseDTO(BaseModel):
    errors: list[ErrorDetail]


class DefaultMessageDTO(BaseModel):
    message: str
