from sqlalchemy.ext.asyncio import AsyncSession
from api.domain.item_model import ItemModel
from api.dto.item_dto import ItemCreateDto

class ItemRepository:
    async def create_item(self, db: AsyncSession, item_data: ItemCreateDto):
        new_item = ItemModel(
            name=item_data.name,
            price=item_data.price
        )
        db.add(new_item)
        await db.commit() 
        await db.refresh(new_item) 
        return new_item