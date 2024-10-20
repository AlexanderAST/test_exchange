import httpx
from fastapi import FastAPI, HTTPException
from api.config import load_config
from datetime import datetime
from api.repository.currency_repository import CurrencyRepository
from api.dto.currency_dto import CurrencyCreateDto
from sqlalchemy.ext.asyncio import AsyncSession

Currencies = ["RUB", "EUR", "USD", "JPY"]

class CurrencyService:
    def __init__(self, currency_repository: CurrencyRepository):
        self.currency_repository = currency_repository

    async def get_currency(self, db: AsyncSession):
        result = []
        try:
            async with httpx.AsyncClient() as client:
                date_today = datetime.today().strftime("%d-%m-%Y")

                for base_currency in Currencies:
                    response = await client.get(f"{load_config().Api.Url}/latest/{base_currency}")
                    response.raise_for_status()
                    data = response.json()

                    currency = CurrencyCreateDto(
                        last_update=date_today,
                        base_code=data.get("base_code"),
                        RUB=f"{data.get('conversion_rates', {}).get('RUB', 0):.2f}",
                        EUR=f"{data.get('conversion_rates', {}).get('EUR', 0):.2f}",
                        USD=f"{data.get('conversion_rates', {}).get('USD', 0):.2f}",
                        JPY=f"{data.get('conversion_rates', {}).get('JPY', 0):.2f}",
                    )

                    result.append(currency)

                    try:
                        await self.currency_repository.create_currency(db, currency)
                    except Exception as e:
                        raise HTTPException(status_code=500, detail=f"Error storing currency data: {str(e)}")

                return result
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"HTTP error: {e.response.text}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
        
    async def currency (self, date: str, db: AsyncSession):
        try:
            result = await self.currency_repository.get_currency(db, date)
            
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"cannot take currency from this date: {date}, {str(e)}")