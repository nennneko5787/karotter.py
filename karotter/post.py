from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from .enums import PostVisibility, ReplyRestriction
from .user import Author


class SmallPost(BaseModel):
    id: int
    createdAt: datetime
    author: Author
    content: str
    mediaTypes: List[str] = []
    mediaUrls: List[str] = []


class Post(SmallPost):
    authorId: int
    parentId: Optional[int] = None
    quotedPostId: Optional[int] = None
    mediaAlts: List[str] = []
    mediaSpoilerFlags: List[bool] = []  # boolじゃないかも
    mediaR18Flags: List[bool] = []  # boolじゃないかも
    embedUrl: Optional[str] = None
    embedTitle: Optional[str] = None
    embedDescription: Optional[str] = None
    embedImage: Optional[str] = None
    likesCount: int
    rekarotsCount: int
    repliesCount: int
    viewsCount: int
    replyRestriction: ReplyRestriction
    replyCircleId: Optional[int] = None
    excludedMentions: List[int] = []  # 型がわからん
    isAiGenerated: bool
    isPromotional: bool
    editedAt: Optional[datetime] = None
    createdAt: datetime
    updatedAt: datetime
    viewerCircleId: Optional[int] = None
    visibility: PostVisibility
    viewerCircle: Optional[int] = None
    replyCircle: Optional[int] = None
    poll: Optional[int] = None  # 型知らん
    bookmarked: bool
    bookmarksCount: int
