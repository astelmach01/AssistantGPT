from typing import List

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AssistantGPT"

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRATION_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRATION_MINUTES: int = 60 * 24 * 7  # 1 week

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
