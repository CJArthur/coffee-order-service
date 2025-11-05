from uuid import UUID

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from structlog import get_logger

from src.api.application.schemas.product import ProductSchema
from src.api.infra.database.common import CreateGate
from src.api.infra.database.tables.product import Product

router = APIRouter(route_class=DishkaRoute)
logger = get_logger()


@router.post("")
async def create_product(
    request: ProductSchema,
    session: FromDishka[AsyncSession],
    create: FromDishka[CreateGate[Product, ProductSchema]],
) -> ProductSchema:
    async with session.begin():
        created = await create.returning()(
            ProductSchema(
                product_id=request.product_id,
                name=request.name,
                price=request.price,
                description=request.description,
                avaibility=request.avaibility,
            )
        )

    return ProductSchema(
        product_id=created.product_id,
        name=created.name,
        price=created.price,
        description=created.description,
        avaibility=created.avaibility,
    )


@router.get("")
async def get_product(product_id: UUID) -> ProductSchema:
    return "200"


@router.patch("")
async def patch_product(
    product_id: UUID,
    request: ProductSchema,
) -> ProductSchema:
    return "200"


@router.delete("")
async def delete_product(product_id: UUID) -> bool:
    return True
