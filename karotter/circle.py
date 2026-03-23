from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from .user import Author


class CircleCountMeta(BaseModel):
    posts: int
    stories: int


class Circle(BaseModel):
    id: int
    ownerId: int
    createdAt: datetime
    updatedAt: datetime
    name: str
    description: Optional[str]
    members: List[Author]
    meta: CircleCountMeta = Field(alias="_count")
