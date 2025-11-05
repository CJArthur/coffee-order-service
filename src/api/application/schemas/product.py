from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True, kw_only=True)
class ProductSchema:
    product_id: UUID
    name: str
    price: float
    description: str
    avaibility: bool
