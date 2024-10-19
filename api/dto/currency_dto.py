from typing import Dict
from pydantic import BaseModel, Field


class CurrencyCreateDto(BaseModel):
    last_update: str
    base_code: str
    RUB: str
    EUR: str
    USD: str
    JPY: str
    model_config = {
        'from_attributes': True 
    } 


class ApiResponce(BaseModel):
    BaseCode: str
    TimeLastUpdateUTC: str
    ConversionRates: Dict[str, float]
    model_config = {
        'from_attributes': True 
    } 

class CurrencyRequest(BaseModel):
    Date: str
    model_config = {
        'from_attributes': True 
    }
    