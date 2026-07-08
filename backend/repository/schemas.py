from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class CreateRepositoryRequest(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: str | None = None
    source: Literal["github", "zip"]


class RepositoryResponse(BaseModel):
    id: str
    user_id: str
    name: str
    description: str | None
    source: str
    status: str
    created_at: datetime