import uuid

from sqlalchemy import UUID, Boolean, Float, String
from sqlalchemy.orm import mapped_column

from src.api.infra.database.tables.base import registry


@registry.mapped_as_dataclass(kw_only=True)
class Product:
    __tablename__ = "products"

    product_id: uuid.UUID = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: str = mapped_column(String(50), nullable=False)
    price: float = mapped_column(Float, nullable=False)
    description: str = mapped_column(String(50))
    avaibility: bool = mapped_column(Boolean, default=True, nullable=False)
