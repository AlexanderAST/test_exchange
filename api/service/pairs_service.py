from fastapi import HTTPException
from api.repository.pairs_repository import PairsRepository 
from sqlalchemy.ext.asyncio import AsyncSession
from api.dto.pairs_dto import PairsDto


class PairsService:
    def __init__(self, pairs_repository: PairsRepository):
        self.pairs_repository = pairs_repository
        
   
    async def get_pairs(self, base: str, currency: str, db: AsyncSession) -> PairsDto:
        try:
            pairs = await self.pairs_repository.get_pairs(db, base)
            if not pairs:
                raise HTTPException(status_code=404, detail="Pairs not found")
            
            result = PairsDto(
                base=pairs.base,
                currency=currency,
                well= "0" 
            )

            if currency == "RUB":
                result.well = pairs.rub
            elif currency == "EUR":
                result.well = pairs.eur
            elif currency == "USD":
                result.well = pairs.usd
            elif currency == "JPY":
                result.well = pairs.jpy
            else:
                raise ValueError(f"Unsupported currency: {currency}")

            return result

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
          