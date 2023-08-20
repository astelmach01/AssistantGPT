from pydantic import BaseModel


class ChatBase(BaseModel):
    prompt: str
