import io
import os
from datetime import datetime
from typing import List, Optional, Union

import httpx

from .enums import Gender, PostVisibility, ReplyRestriction
from .http import KarotterHTTP
from .post import Post
from .responses import LoginResponse
from .user import ClientUser, User

__all__ = ("Karotter",)


class Karotter:
    def __init__(self, *, http: Optional[httpx.AsyncClient] = None):
        self.http: KarotterHTTP = KarotterHTTP(http)
        self.clientUser: Optional[ClientUser] = None
        self.user: Optional[User] = None

    async def login(
        self, identifier: str, password: str, gender: Gender
    ) -> LoginResponse:
        """アカウントにログインします。

        Parameters
        ----------
        identifier : str
            アカウントのメールアドレスまたはユーザーネーム。
        password : str
            アカウントのパスワード。
        gender : Gender
            アカウントの性別。

        Returns
        -------
        LoginResponse
            ログイン時のレスポンス。
        """

        response = await self.http.login(identifier, password, gender)
        self.clientUser = response.user

        self.user = await self.http.me()
        return response

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
        """投稿を作成します。

        Parameters
        ----------
        content : str
            投稿の本文。
        isAiGenerated : bool, optional
            AI生成された投稿であるかどうか, by default False
        isPromotional : bool, optional
            ブランドやビジネスの宣伝であるかどうか, by default False
        visibility : PostVisibility, optional
            投稿の公開範囲, by default PostVisibility.PUBLIC
        viewerCircleId : Optional[int], optional
            投稿を公開するサークルのID、visibilityがPostVisibility.CIRCLEのときのみ指定可能, by default None
        replyRestriction : ReplyRestriction, optional
            返信を許可するユーザーの範囲, by default ReplyRestriction.EVERYONE
        replyCircleId : Optional[int], optional
            返信を許可するサークルのID、replyRestrictionがReplyRestriction.CIRCLEのときのみ指定可能, by default None
        mediaAlts : Optional[List[str]], optional
            添付ファイルの代替テキスト, by default None
        mediaSpoilerFlags : Optional[List[bool]], optional
            添付ファイルのネタバレフラグ, by default None
        mediaR18Flags : Optional[List[bool]], optional
            添付ファイルのNSFWフラグ, by default None
        pollOptions : Optional[List[str]], optional
            投票の選択肢, by default None
        pollDurationHours : Optional[int], optional
            投票可能な時間, by default None
        scheduledFor : Optional[datetime], optional
            ポストを予約投稿する時間, by default None
        media : Optional[Union[os.PathLike, io.BufferedIOBase]], optional
            添付ファイル, by default None

        Returns
        -------
        Post
            作成した投稿。
        """

        return await self.http.createPost(
            content,
            isAiGenerated=isAiGenerated,
            isPromotional=isPromotional,
            visibility=visibility,
            viewerCircleId=viewerCircleId,
            replyRestriction=replyRestriction,
            replyCircleId=replyCircleId,
            mediaAlts=mediaAlts,
            mediaSpoilerFlags=mediaSpoilerFlags,
            mediaR18Flags=mediaR18Flags,
            pollOptions=pollOptions,
            pollDurationHours=pollDurationHours,
            scheduledFor=scheduledFor,
            media=media,
        )
