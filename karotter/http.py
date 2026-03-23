import io
import json
import os
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

import karotter

from .constants import Constants
from .enums import Gender, PostVisibility, ReplyRestriction
from .exceptions import KarotterClientError, KarotterServerError
from .post import Post
from .responses import LoginResponse, UserResponse
from .user import Me, User

__all__ = ("KarotterHTTP",)


class KarotterHTTP:
    def __init__(
        self,
        http: Optional[httpx.AsyncClient] = None,
        *,
        apiKey: Optional[str] = None,
    ):
        self.http: httpx.AsyncClient = http or httpx.AsyncClient(
            headers={"user-agent": f"karotter.py/{karotter.__version__}"}
        )
        self.http.headers.update({"X-Client-Type": "web"})
        self.http.base_url = "https://karotter.com/api/"

        self.apiKey: Optional[str] = apiKey

    async def get(
        self,
        url: str,
        *,
        params: Optional[Dict[Any, Any]] = None,
        csrf: bool = False,
        **kwargs,
    ) -> Dict[str, str]:
        if self.apiKey:
            self.http.headers.update({"Authorization": self.apiKey})
        elif csrf:
            self.http.headers.update({"X-Csrf-Token": await self.getCSRFToken()})

        response = await self.http.get(url, params=params, **kwargs)

        if response.status_code >= 400 and response.status_code <= 499:
            raise KarotterClientError(response.status_code, response.text)
        if response.status_code >= 500 and response.status_code <= 599:
            raise KarotterServerError(response.status_code, response.text)

        return response.json()

    async def post(
        self,
        url: str,
        *,
        headers: Optional[Dict[Any, Any]] = None,
        json: Optional[Any] = None,
        data: Optional[Any] = None,
        csrf: bool = False,
        **kwargs,
    ) -> Dict[str, str]:
        if self.apiKey:
            self.http.headers.update({"Authorization": self.apiKey})
        elif csrf:
            self.http.headers.update({"X-Csrf-Token": await self.getCSRFToken()})

        response = await self.http.post(
            url, headers=headers, json=json, data=data, **kwargs
        )

        if response.status_code >= 400 and response.status_code <= 499:
            raise KarotterClientError(response.status_code, response.text)
        if response.status_code >= 500 and response.status_code <= 599:
            raise KarotterServerError(response.status_code, response.text)

        return response.json()

    async def getCSRFToken(self):
        return (await self.get("auth/csrf-token"))["csrfToken"]

    async def login(
        self, identifier: str, password: str, gender: Gender
    ) -> LoginResponse:
        if self.apiKey:
            raise NotImplementedError("APIキー使用時はログインAPIを利用できません。")

        deviceId = str(uuid.uuid4())
        self.http.headers.update({"X-Device-Id": deviceId})
        response = await self.post(
            "auth/login",
            json={
                "identifier": identifier,
                "password": password,
                "gender": gender.value,
                "deviceId": deviceId,
                "clientType": "web",
                "deviceName": Constants.DEVICE_NAME,
            },
        )
        return LoginResponse.model_validate(response)

    async def me(self) -> Me:
        response = await self.get(
            "auth/me",
        )

        return Me.model_validate(response["user"])

    async def createPost(
        self,
        content: str,
        *,
        isAiGenerated: bool = False,
        isPromotional: bool = False,
        visibility: PostVisibility = PostVisibility.PUBLIC,
        viewerCircleId: Optional[int] = None,
        replyRestriction: ReplyRestriction = ReplyRestriction.EVERYONE,
        replyCircleId: Optional[int] = None,
        mediaAlts: Optional[List[str]] = None,
        mediaSpoilerFlags: Optional[List[bool]] = None,
        mediaR18Flags: Optional[List[bool]] = None,
        pollOptions: Optional[List[str]] = None,
        pollDurationHours: Optional[int] = None,
        scheduledFor: Optional[datetime] = None,
        media: Optional[Union[os.PathLike, io.BufferedIOBase]] = None,
    ) -> Post:
        data: dict[str, Any] = {
            "content": content,
            "isAiGenerated": isAiGenerated,
            "isPromotional": isPromotional,
            "visibility": visibility.value,
            "replyRestriction": replyRestriction.value,
            "mediaAlts": json.dumps(mediaAlts) if mediaAlts else "[]",
            "mediaSpoilerFlags": json.dumps(mediaSpoilerFlags)
            if mediaSpoilerFlags
            else "[]",
            "mediaR18Flags": json.dumps(mediaR18Flags) if mediaR18Flags else "[]",
        }

        if visibility == PostVisibility.CIRCLE:
            data.update({"viewerCircleId": viewerCircleId})
        if replyRestriction == ReplyRestriction.CIRCLE:
            data.update({"replyCircleId": replyCircleId})
        if pollOptions:
            data.update({"pollOptions": json.dumps(pollOptions)})
        if pollDurationHours:
            data.update({"pollDurationHours": pollDurationHours})
        if scheduledFor:
            data.update({"scheduledFor": scheduledFor.isoformat()})

        f = None
        if isinstance(media, os.PathLike):
            f = open(os.fspath(media), "rb")
            data.update({"media": f})
        elif isinstance(media, io.BufferedIOBase):
            data.update({"media": media})

        jsonData = await self.post(
            "posts",
            data=data,
            csrf=True,
        )

        if f:
            f.close()

        return Post.model_validate(jsonData["post"])

    async def getUserByUserName(self, userName: str) -> UserResponse:
        return UserResponse.model_validate(await self.get(f"users/{userName}"))
