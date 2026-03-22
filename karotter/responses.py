from typing import Any, List

from pydantic import BaseModel

from .user import User


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
