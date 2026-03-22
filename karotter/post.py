from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from .enums import PostVisibility, ReplyRestriction
from .user import Author

__all__ = (
    "SmallPost",
    "PollOption",
    "Poll",
    "Post",
)


class SmallPost(BaseModel):
    id: int
    createdAt: datetime
    author: Author
    content: str
    mediaTypes: List[str] = []
    mediaUrls: List[str] = []


class PollOption(BaseModel):
    id: int
    text: str
    position: int
    votesCount: int
    percentage: int
    votedByMe: bool


class Poll(BaseModel):
    id: int
    expiresAt: datetime
    isExpired: bool
    totalVotes: int
    ownVoteOptionId: Optional[int] = None
    options: List[PollOption] = []


class Post(SmallPost):
    authorId: int
    parentId: Optional[int] = None
    quotedPostId: Optional[int] = None
    mediaAlts: List[str] = []
    mediaSpoilerFlags: List[bool] = []
    mediaR18Flags: List[bool] = []
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
    poll: Optional[Poll] = None
    bookmarked: bool
    bookmarksCount: int
