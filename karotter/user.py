from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from .enums import Gender, OnlineStatus, Visibility

__all__ = (
    "ClientUser",
    "Author",
    "User",
)


class ClientUser(BaseModel):
    id: int
    username: str
    displayName: str
    email: str
    avatarUrl: Optional[str] = None
    emailVerified: bool


class Author(BaseModel):
    id: int
    username: str
    displayName: str
    avatarUrl: Optional[str] = None
    avatarFrameId: Optional[int] = None
    isPrivate: bool = False


class User(Author):
    pinnedPostId: Optional[int] = None
    headerUrl: Optional[str] = None
    bio: Optional[str] = None
    birthday: Optional[str] = None
    birthdayVisibility: Visibility
    birthdayBalloonsEnabled: bool
    gender: Gender
    officialMark: str  # 知らん後でまとめる
    websiteUrl: Optional[str] = None
    location: Optional[str] = None
    onlineStatus: OnlineStatus
    statusMessage: Optional[str] = None
    onlineStatusVisibility: Visibility
    followersCount: int
    followingCount: int
    postsCount: int
    isPremium: bool
    createdAt: datetime
    userBadges: List[str] = []
    age: Optional[int] = None
    badges: List[str] = []
