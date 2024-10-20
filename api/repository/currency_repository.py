from sqlalchemy.ext.asyncio import AsyncSession
from api.domain.currency_model import CurrencyModel
from api.dto.currency_dto import CurrencyCreateDto
from sqlalchemy import select


class CurrencyRepository:
    async def create_currency(self, db:AsyncSession, currency_data: CurrencyCreateDto):
        new_currency = CurrencyModel(
            last_update = currency_data.last_update,
            base = currency_data.base_code,
            rub = currency_data.RUB,
            eur = currency_data.EUR, 
            usd = currency_data.USD, 
            jpy = currency_data.JPY
        )

        db.add(new_currency)
        await db.commit()
        await db.refresh(new_currency)
        return new_currency
    
    async def get_currency(self, db: AsyncSession, date: str):
        query = select(CurrencyModel).where(CurrencyModel.last_update == date)
        result = await db.execute(query)
        
        return result.scalars().all()