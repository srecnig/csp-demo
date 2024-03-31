from flask import redirect, request, url_for

from bad_code.bad_blog.db import Comment, Post, get_db

from .. import blueprint
from .naive_templating import naive_index_template, naive_post_template


@blueprint.route("/")
def index():
    db = get_db()
    posts = [
        Post(post_id=row["post_id"], title=row["title"], body=row["body"], comments=[])
        for row in db.execute("SELECT * FROM post").fetchall()
    ]
    return naive_index_template(posts)


@blueprint.route("/<int:post_id>", methods=("GET",))
def post(post_id: int):
    db = get_db()
    comment_rows = db.execute("SELECT * FROM comment WHERE post_id = ? ORDER BY created_at DESC", (post_id,)).fetchall()
    post_row = db.execute("SELECT * FROM post WHERE post_id = ?", (post_id,)).fetchone()
    post = Post(
        post_id=post_row["post_id"],
        title=post_row["title"],
        body=post_row["body"],
        comments=[
            Comment(
                comment_id=comment_row["comment_id"],
                title=comment_row["title"],
                body=comment_row["body"],
            )
            for comment_row in comment_rows
        ],
    )
    return naive_post_template(post)


@blueprint.route("/<int:post_id>/add-comment", methods=("POST",))
def add_comment(post_id):
    db = get_db()
    db.execute(
        "INSERT INTO comment (post_id, title, body) VALUES (?, ?, ?)",
        (post_id, request.form["title"], request.form["body"]),
    )
    db.commit()
    return redirect(url_for(".post", post_id=post_id))
