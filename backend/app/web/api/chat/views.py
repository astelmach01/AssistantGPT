from fastapi import APIRouter
from schemas.chat import ChatBase

router = APIRouter()


@router.post("/request")
async def chat(chat_request: ChatBase):
    return {"chat": chat_request.prompt}
