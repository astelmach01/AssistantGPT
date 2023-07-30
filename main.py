import os

import uvicorn

from app.main import app
from app.settings import settings

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    reload = settings.environment != "prod"

    uvicorn.run(app, host="0.0.0.0", port=port, reload=reload)
