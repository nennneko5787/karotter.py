from enum import StrEnum


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
