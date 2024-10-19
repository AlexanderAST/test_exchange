from pydantic import BaseModel, Field

class ItemCreateDto(BaseModel):
    name: str
    price: float

    model_config = {
        'from_attributes': True 
    }

class ItemResponseDto(BaseModel):
    id: int
    name: str
    price: float

    model_config = {
        'from_attributes': True 
    }
