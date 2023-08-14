from typing import Awaitable, Callable

from app.db.config import database
from app.db.meta import meta
from app.db.models import load_all_models
from app.services.rabbit.lifetime import init_rabbit, shutdown_rabbit
from app.settings import settings
from fastapi import FastAPI
from sqlalchemy.engine import create_engine


async def _create_tables() -> None:  # pragma: no cover
    """Populates tables in the database."""
    load_all_models()
    engine = create_engine(str(settings.db_url))
    with engine.connect() as connection:
        meta.create_all(connection)
    engine.dispose()


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    in the state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("startup")
    async def _startup() -> None:  # noqa: WPS430
        app.middleware_stack = None
        await database.connect()
        await _create_tables()
        init_rabbit(app)
        app.middleware_stack = app.build_middleware_stack()
        pass  # noqa: WPS420

    return _startup


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application's shutdown.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("shutdown")
    async def _shutdown() -> None:  # noqa: WPS430
        await database.disconnect()
        await shutdown_rabbit(app)
        pass  # noqa: WPS420

    return _shutdown
