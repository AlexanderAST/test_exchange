from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from fastapi import HTTPException
from datetime import datetime
import re


class ValidateDate(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
           
    async def dispatch(self, request:Request, call_next: RequestResponseEndpoint) -> Response:
        
        if request.method == "GET" and re.match(r"^/currency/\d{2}-\d{2}-\d{4}$", request.url.path):
            date_str = request.url.path.split("/")[-1]
            print("AAAAAAAAAAAAAAA")
            try:
                datetime.strptime(date_str, "%d-%m-%Y")
            except ValueError:
                raise HTTPException(status_code=400, detail="invalide timeformat")
        
        response = await call_next(request)
        return response