from fastapi import FastAPI, APIRouter
from api.controller import hello_controller
from api.controller import item_controller
from api.controller import currency_controller
from api.controller import pairs_controller
from api.middleware.check_name_middleware import CheckNameMiddleware
from api.middleware.date_middleware import ValidateDate

app = FastAPI()


app.add_middleware(CheckNameMiddleware, restricted_name="Laptop")
app.add_middleware(ValidateDate)

app.include_router(hello_controller.router)
app.include_router(item_controller.router)
app.include_router(currency_controller.router)
app.include_router(pairs_controller.router)