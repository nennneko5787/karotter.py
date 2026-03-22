from typing import Any, List

from pydantic import UUID4, BaseModel

from .user import ClientUser, User

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
    mutualFollowersPreview: List[User] = []  # わんちゃんidかも？
    mutualFollowersCount: int
    pinnedPost: List[Any]  # あとで投稿をクラス化する
