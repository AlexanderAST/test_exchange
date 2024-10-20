from pydantic import BaseModel


class PairsDto(BaseModel):
    base: str
    currency: str
    well: str