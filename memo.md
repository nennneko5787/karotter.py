# memo

## 大前提

- **このメモにあるエンドポイント/型は実装され次第消えます。そのため正確なものではないことをご承知ください。**

- `base_url`は`https://karotter.com/api/`
- デフォルト値はあくまでもクライアントのデフォルトであり指定しなくても良いわけではないので注意。逆に言えばAPI実装はこれらのデフォルトを尊重すべきである。
- ユーザー認証は`Authorization`ヘッダーではなく`Cookie`ヘッダーで行う。こちらはログイン時に返ってくるクッキーをセットする。
- Post型、User型には通知向けに簡略化されたバージョンがあるようである。クラスの継承などで実装することをおすすめする。

## ガチどうでもいいこと

- サーバーが重い
- どうやら、強制SSL化が行われていないらしい。Cloudflareなのに。
- ~~ユーザーネームからユーザーを取得するAPIはないのか。~~ あった。

## 型

### PostVisibility (Enum)

- PUBLIC `誰でも投稿を見ることができます。`
- CIRCLE `投稿を見るためにはサークルへの所属が必要です。`

### ReplyRestriction (Enum)

- EVERYONE `誰でも投稿に返信することができます。`
- FOLLOWING `フォロー中の人は投稿に返信することができます。`
- MENTIONED `メンションされている人は投稿に返信することができます。`
- CIRCLE `サークルのメンバーは投稿に返信することができます。`

## エンドポイント

### GET users/[username:str]

ユーザーネームからユーザーを取得する。

response: たぶんuser (500エラーで見れない)

### POST social/circles

サークルを作成する。

request:

```json
{
  "name": "str: サークルの名前"
}
```

response:

```json
{
  "circle": {
    "id": "int サークルのID",
    "ownerId": "int 作成者のID",
    "name": "str",
    "description": "Optional[str]",
    "createdAt": "datetime",
    "updatedAt": "datetime"
  }
}
```

### POST posts

投稿を作成する。  
他のエンドポイントと違い`Content-type`が`multipart/form-data`なので注意。

request:

```
content: str
本文。全角半角問わず200文字まで。
isAiGenerated: bool = false
AIで生成された投稿であるかどうか。
isPromotional: bool = false
ブランドかビジネスの宣伝かどうか。
visibility: Visibility = PostVisibility.PUBLIC
投稿の公開範囲。
[If visivility = PostVisibility.CIRCLE] viewerCircleId: int
投稿を公開するサークル。
replyRestriction: ReplyRestriction = ReplyRestriction.EVERYONE
返信できるユーザーの範囲。
[If replyRestriction = ReplyRestriction.CIRCLE] replyCircleId: int
返信を許可するサークル。
mediaAlts: List[str] = []
添付ファイルの代替テキスト。
mediaSpoilerFlags: List[bool] = []
添付ファイルの"ネタバレ"タグ。
mediaR18Flags: List[bool] = []
添付ファイルの"NSFW"タグ。

[undefinedable] pollOptions: List[str]
投票の選択肢。JSONと同じListで指定できる。
[If pollOptions !== undefined] pollDurationHours: int
投票可能な時間。

[undefinedable] scheduledFor: datetime
ポストを予約する時間。投票時間と異なりこちらはdatetime。

[undefinedable] media: bytes
動画もしくは画像。
```

response:

postクラスを実装するまでここにpostデータをそのまま貼っておく。

```json
{
  "message": "投稿しました",
  "post": {
    "id": 839,
    "content": "多分すぐ過疎るSNSだろうからhttp見てんだけど、AuthorとActorが地味に違うのめんどくさいな。まあ名前違うから当たり前なんだけど。",
    "authorId": 148,
    "parentId": null,
    "quotedPostId": null,
    "mediaUrls": [],
    "mediaTypes": [],
    "mediaAlts": [],
    "mediaSpoilerFlags": [],
    "mediaR18Flags": [],
    "embedUrl": null,
    "embedTitle": null,
    "embedDescription": null,
    "embedImage": null,
    "likesCount": 0,
    "rekarotsCount": 0,
    "repliesCount": 0,
    "viewsCount": 0,
    "replyRestriction": "EVERYONE",
    "replyCircleId": null,
    "excludedMentions": [],
    "isAiGenerated": false,
    "isPromotional": false,
    "editedAt": null,
    "createdAt": "2026-03-22T12:14:45.079Z",
    "updatedAt": "2026-03-22T12:14:45.079Z",
    "viewerCircleId": null,
    "visibility": "PUBLIC",
    "author": {
      "id": 148,
      "username": "Fng1Popn",
      "displayName": "ねんねこ",
      "avatarUrl": "/uploads/avatars/avatar_148_1774179474450.webp",
      "avatarFrameId": null,
      "isPrivate": false
    },
    "viewerCircle": null,
    "replyCircle": null,
    "poll": null,
    "bookmarked": false,
    "bookmarksCount": 0
  }
}
```
