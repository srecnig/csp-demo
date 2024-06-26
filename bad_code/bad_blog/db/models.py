import dataclasses


@dataclasses.dataclass
class Comment:
    comment_id: int
    title: str
    body: str


@dataclasses.dataclass
class Post:
    post_id: int
    title: str
    body: str
    comments: list[Comment]
