from enum import StrEnum

__all__ = (
    "Visibility",
    "PostVisibility",
    "ReplyRestriction",
    "Gender",
    "OnlineStatus",
    "OfficialMark",
    "ReplySource",
)


class Visibility(StrEnum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"


class PostVisibility(StrEnum):
    PUBLIC = "PUBLIC"
    CIRCLE = "CIRCLE"


class ReplyRestriction(StrEnum):
    EVERYONE = "EVERYONE"
    FOLLOWING = "FOLLOWING"
    MENTIONED = "MENTIONED"
    CIRCLE = "CIRCLE"


class Gender(StrEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class OnlineStatus(StrEnum):
    OFFLINE = "OFFLINE"
    IDLE = "IDLE"
    DND = "DND"
    ONLINE = "ONLINE"


class OfficialMark(StrEnum):
    NONE = "NONE"
    BLUE = "BLUE"
    YELLOW = "YELLOW"
    PURPLE = "PURPLE"


class ReplySource(StrEnum):
    THREAD_PARTICIPANT = "THREAD_PARTICIPANT"
