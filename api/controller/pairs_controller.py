from fastapi import APIRouter, HTTPException, Depends
from api.service.pairs_service import PairsService
from api.repository.pairs_repository import PairsRepository
from sqlalchemy.ext.asyncio import AsyncSession
from api.database import get_db

router = APIRouter()
pairs_service = PairsService(PairsRepository())


@router.get("/pairs")
async def get_pairs(base: str = "", currency: str = "", db: AsyncSession = Depends(get_db)):
     try:
      result = await pairs_service.get_pairs(base.upper(),currency.upper(), db)
      return {"pairs": result}
     except HTTPException as e:
        raise e
     except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
