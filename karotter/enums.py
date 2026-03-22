from enum import StrEnum


class Visibility(StrEnum):
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"


class Gender(StrEnum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"


class OnlineStatus(StrEnum):
    OFFLINE = "OFFLINE"
    IDLE = "IDLE"
    DND = "DND"
    ONLINE = "ONLINE"
