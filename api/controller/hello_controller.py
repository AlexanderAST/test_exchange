from fastapi import APIRouter

router = APIRouter()


@router.get("/hello")
async def say_hello():
    return {"hello":"hello world!"}