from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from fastapi import HTTPException

class CheckNameMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, restricted_name: str):
        super().__init__(app)
        self.restricted_name = restricted_name

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        if request.method == "POST" and request.url.path == "/items":
            body = await request.json()
            if body.get("name") == self.restricted_name:
                raise HTTPException(status_code=400, detail=f"The name '{self.restricted_name}' is not allowed.")
        response = await call_next(request)
        return response
