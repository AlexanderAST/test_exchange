from sqlalchemy.ext.asyncio import AsyncSession
from api.domain.currency_model import CurrencyModel
from sqlalchemy import select


class PairsRepository:
    async def get_pairs(self, db: AsyncSession, base: str):
        query = select(CurrencyModel).where(CurrencyModel.base == base)
        result = await db.execute(query)
        
        return result.scalars().first()