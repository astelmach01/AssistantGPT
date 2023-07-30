import os

import uvicorn

from app.main import app
from app.settings import settings

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))

    uvicorn.run(app, host="0.0.0.0", port=port)
