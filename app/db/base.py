from app.db.config import database
from app.db.meta import meta
from ormar import ModelMeta


class BaseMeta(ModelMeta):
    """Base metadata for models."""

    database = database
    metadata = meta
