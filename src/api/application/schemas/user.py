from dataclasses import dataclass
from uuid import UUID

@dataclass(slots=True, kw_only=True)
class UserSchema:
    user_id: UUID
    username: str
    number: int

@dataclass(slots=True)
class UserRequest:
    username: str
    number: int

