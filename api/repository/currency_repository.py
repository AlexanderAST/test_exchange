from sqlalchemy.ext.asyncio import AsyncSession
from api.domain.currency_model import CurrencyModel
from api.dto.currency_dto import CurrencyCreateDto


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