from fastapi import FastAPI
from api.controller import hello_controller
from api.controller import item_controller

app = FastAPI()

app.include_router(hello_controller.router)
app.include_router(item_controller.router)