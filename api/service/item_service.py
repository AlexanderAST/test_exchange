from sqlalchemy.ext.asyncio import AsyncSession
from api.repository.item_repository import ItemRepository
from api.dto.item_dto import ItemCreateDto

class ItemService:
    def __init__(self, item_repository: ItemRepository):
        self.item_repository = item_repository

    async def create_item(self, db: AsyncSession, item_data: ItemCreateDto):
        return await self.item_repository.create_item(db, item_data)