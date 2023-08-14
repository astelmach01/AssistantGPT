from app.web.api import docs, monitoring
from fastapi.routing import APIRouter

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
