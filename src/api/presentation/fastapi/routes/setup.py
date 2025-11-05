from fastapi import FastAPI
from structlog import get_logger

from src.api.presentation.fastapi.routes.healthcheck import (
    router as healthcheck_router,
)
from src.api.presentation.fastapi.routes.products import (
    router as product_router,
)

logger = get_logger()


def setup_routes(app: FastAPI) -> None:
    app.include_router(healthcheck_router)
    app.include_router(product_router, prefix="/product", tags=["Product"])
    logger.info("routes set up")
