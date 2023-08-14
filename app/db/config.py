from app.settings import settings
from databases import Database

database = Database(str(settings.db_url))
