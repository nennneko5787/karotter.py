from typing import List, Optional

from pydantic import UUID4, BaseModel

from .post import PinnedPost
from .user import Author, ClientUser, User

__all__ = (
    "UserResponse",
    "LoginResponse",
)


class LoginResponse(BaseModel):
    accessToken: str
    sessionId: UUID4
    deviceId: UUID4
    user: ClientUser


class UserResponse(BaseModel):
    user: User
    isFollowing: bool
    isFollowedBy: bool
    isBlocked: bool
    hasBlocked: bool
    isBlockedBy: bool
    isMuted: bool
    hasPendingRequest: bool
    mutualFollowersPreview: List[Author] = []
    mutualFollowersCount: int
    pinnedPost: Optional[PinnedPost] = None
