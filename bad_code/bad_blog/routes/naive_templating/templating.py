from flask import url_for

from bad_code.bad_blog.db import Comment, Post


def naive_index_template(posts: list[Post]):
    posts_html = "\n".join(
        [
            f"<li><a href=\"{ url_for('.post', post_id=post.post_id)  }\">{post.post_id} {post.title}</li>"
            for post in posts
        ]
    )
    body_html = f"""<h1>Posts</h1>
    <ul>{posts_html}</ul>"""
    return naive_html_base_template(body_html)


def naive_post_template(post: Post):
    comments_html = "\n".join([naive_comment_template(comment) for comment in post.comments])
    body_html = f"""<h1>{post.title}</h1>
    {post.body}
    <hr>
    <h2>Comments</h2>
    {naive_comment_form(post)}
    {comments_html}
"""
    return naive_html_base_template(body_html)


def naive_comment_form(post: Post):
    return f"""<form method="post" action="/{post.post_id}/add-comment">
    <label for="title">Title</label><br>
    <input type="text" name="title" placeholder="Title"><br>
    <label for="title">Your comment</label><br>
    <textarea name="body" placeholder="Tell us what you like"></textarea><br>
    <input type="submit" value="Submit">"""


def naive_comment_template(comment: Comment):
    comment_html = f"""<h3>{comment.title}</h3>
    <p>{comment.body}</p>
"""
    return comment_html


def naive_html_base_template(body: str):
    return f"""<html>
<head>
    <title>really bad blog</title>
</head>
<body>
    {body}
</body>
</html>"""
