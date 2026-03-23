from datetime import datetime
from typing import Any, List, Literal, Optional

from pydantic import BaseModel

from .circle import Circle
from .enums import PostVisibility, ReplyRestriction, ReplySource
from .user import Author

__all__ = (
    "SmallPost",
    "PollOption",
    "Poll",
    "BasePost",
    "Post",
    "PinnedPost",
    "ReplyTarget",
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


class ReplyTarget(BaseModel):
    id: int
    postId: int
    userId: int
    source: ReplySource
    createdAt: datetime
    user: Author


class ReactionSummary(BaseModel):
    emoji: str
    count: int
    reacted: bool


class CommonPostFields(SmallPost):
    parentId: Optional[int] = None
    quotedPostId: Optional[int] = None
    mediaAlts: List[str] = []
    mediaSpoilerFlags: List[bool] = []
    mediaR18Flags: List[bool] = []
    likesCount: int
    rekarotsCount: int
    repliesCount: int
    replyCircleId: Optional[int] = None
    excludedMentions: List[int] = []  # 型がわからん
    isAiGenerated: bool
    isPromotional: bool
    editedAt: Optional[datetime] = None
    createdAt: datetime
    viewerCircleId: Optional[int] = None
    viewerCircle: Optional[int] = None
    replyCircle: Optional[Circle] = None
    poll: Optional[Poll] = None
    replyToUsers: List[Author] = []
    replyTargets: List[ReplyTarget] = []
    reactionSummary: List[ReactionSummary] = []
    reactionsCount: int
    comment: Optional[str] = None
    itemId: str
    quoteUsersCount: int
    rekaroted: bool
    rekarotedBy: Optional[Author] = None
    rekarots: List[Any] = []
    time: datetime


class BasePost(CommonPostFields):
    authorId: int
    updatedAt: datetime
    replyRestriction: ReplyRestriction
    viewsCount: int
    bookmarked: bool
    bookmarksCount: int
    canInteract: bool
    canQuote: bool
    hasBlockedAuthor: bool
    isMutedByViewer: bool
    visibility: PostVisibility
    type: Literal["REKAROT", "POST"]


class Post(BasePost):
    embedUrl: Optional[str] = None
    embedTitle: Optional[str] = None
    embedDescription: Optional[str] = None
    embedImage: Optional[str] = None


class PinnedPost(CommonPostFields):
    type: Literal["POST"]
