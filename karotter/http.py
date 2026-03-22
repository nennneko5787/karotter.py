import io
import json
import os
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from . import constants as Constants
from .enums import Gender, PostVisibility, ReplyRestriction
from .exceptions import KarotterClientError, KarotterServerError
from .post import Post
from .responses import LoginResponse
from .user import User

__all__ = ("KarotterHTTP",)


class KarotterHTTP:
    def __init__(self, http: Optional[httpx.AsyncClient] = None):
        self.http: httpx.AsyncClient = http or httpx.AsyncClient()
        self.http.base_url = "https://karotter.com/api/"
        self.loginResponse: Optional[LoginResponse] = None

    async def get(
        self,
        url: str,
        *,
        params: Optional[Dict[Any, Any]] = None,
        csrf: bool = False,
        **kwargs,
    ) -> Dict[str, str]:
        if csrf:
            self.http.headers.update({"X-Csrf-Token": await self.getCSRFToken()})

        if self.loginResponse:
            self.http.headers.update(
                {"Authorization": f"Bearer {self.loginResponse.accessToken}"}
            )

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
        if csrf:
            self.http.headers.update({"X-Csrf-Token": await self.getCSRFToken()})

        if self.loginResponse:
            self.http.headers.update(
                {"Authorization": f"Bearer {self.loginResponse.accessToken}"}
            )

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
        deviceId = str(uuid.uuid4())
        self.http.headers.update({"X-Client-Type": "web"})
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
        self.loginResponse = LoginResponse.model_validate(response)
        return self.loginResponse

    async def me(self) -> User:
        response = await self.get(
            "auth/me",
        )

        return User.model_validate(response["user"])

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
            "content": "content",
            "isAiGenerated": isAiGenerated,
            "isPromotional": isPromotional,
            "visibility": visibility.value,
            "replyRestriction": replyRestriction.value,
            "mediaAlts": json.dumps(mediaAlts) if mediaAlts else "[]",
            "mediaSpoilerFlags": json.dumps(mediaAlts) if mediaAlts else "[]",
            "mediaR18Flags": json.dumps(mediaAlts) if mediaAlts else "[]",
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

        print(data)

        jsonData = await self.post(
            "posts",
            headers={"Content-type": "multipart/form-data"},
            data=data,
            csrf=True,
        )

        if f:
            f.close()

        return Post.model_validate(jsonData["post"])
