from fastapi.routing import APIRouter

from .docs import router as docs_router
from .monitoring import router as monitoring_router

api_router = APIRouter()
api_router.include_router(monitoring_router)
api_router.include_router(docs_router)
