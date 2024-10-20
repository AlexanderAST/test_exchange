from fastapi import APIRouter, HTTPException, Depends
from api.service.currency_service import CurrencyService
from api.repository.currency_repository import CurrencyRepository
from api.database import get_db
from api.dto.currency_dto import CurrencyCreateDto
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()
currency_service = CurrencyService(CurrencyRepository())


@router.get("/getCurrency")
async def create_currency(db: AsyncSession = Depends(get_db)):
   try:
      data = await currency_service.get_currency(db)
      return {"message":"currency", "currency":data}
   except HTTPException as e:
      raise e
   
   except HTTPException as e:
      raise HTTPException(status_code=500, detail=str(e))
   

@router.get("/currency/{date}")
async def currency(date:str, db: AsyncSession = Depends(get_db)):
   try:
      result = await currency_service.currency(date, db)
      return {"currencies": result}
   except HTTPException as e:
      raise e
   except Exception as e:
      raise HTTPException(status_code=500, detail=str(e))