import uuid
from typing import Annotated

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from structlog import get_logger

from src.api.infra.database.common import CreateGate
from src.api.infra.database.core.document.schema import UserSchema
from src.api.infra.database.tables.document import Users
from src.api.infra.s3.products import ProductS3Gate
from src.api.application.schemas.user import UserRequest
router = APIRouter(route_class=DishkaRoute)
logger = get_logger()


@router.post("/auth", response_model=None)
async def auth(
    session: FromDishka[AsyncSession],
    create: FromDishka[CreateGate[User, UserSchema]],
    user: UserRequest
) -> UserSchema:
    filename = file.filename or f"document-{uuid.uuid4()}"
    content_type = file.content_type or "application/octet-stream"
    size = file.size or 0

    async with session.begin():
        await s3_gate.upload_file(filename, file.file, content_type)
        created = await create.returning()(
            DocumentSchema(
                path=f"{s3_gate.config.base_url}/{s3_gate.config.bucket_name}/{s3_gate.path_prefix}/{filename}",
                file_type=content_type[content_type.find("/") + 1 :],
                size=size,
                mime_type=content_type,
            )
        )

    return created

