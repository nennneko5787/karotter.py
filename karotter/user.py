from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from .enums import Gender, OnlineStatus, Visibility

"""
{
    "user": {
        "id": 193,
        "username": "HIKAKIN",
        "displayName": "HIKAKIN 公式",
        "avatarUrl": "/uploads/avatars/avatar_193_1774174773063.webp",
        "avatarFrameId": null,
        "pinnedPostId": null,
        "headerUrl": null,
        "bio": "ヒカキンですよ。",
        "birthday": null,
        "birthdayVisibility": "PRIVATE",
        "birthdayBalloonsEnabled": true,
        "gender": "OTHER",
        "officialMark": "NONE",
        "websiteUrl": "",
        "location": null,
        "isPrivate": false,
        "onlineStatus": "OFFLINE",
        "statusMessage": null,
        "onlineStatusVisibility": "PUBLIC",
        "followersCount": 1,
        "followingCount": 0,
        "postsCount": 1,
        "isPremium": false,
        "createdAt": "2026-03-22T10:18:35.750Z",
        "userBadges": [],
        "age": null,
        "badges": []
    },
    "isFollowing": true,
    "isFollowedBy": false,
    "isBlocked": false,
    "hasBlocked": false,
    "isBlockedBy": false,
    "isMuted": false,
    "hasPendingRequest": false,
    "mutualFollowersPreview": [],
    "mutualFollowersCount": 0,
    "pinnedPost": null
}
"""


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
    websiteUrl: str
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
