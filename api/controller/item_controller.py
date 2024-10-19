from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from api.service.item_service import ItemService
from api.dto.item_dto import ItemCreateDto, ItemResponseDto
from api.database import get_db
from api.repository.item_repository import ItemRepository

router = APIRouter()
item_service = ItemService(ItemRepository())

@router.post("/items", response_model=ItemResponseDto)
async def create_item(item: ItemCreateDto, db: AsyncSession = Depends(get_db)):
    try:
        
        created_item = await item_service.create_item(db, item)  
        return ItemResponseDto.model_validate(created_item)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))