from flask import url_for
from bad_code.bad_blog.db import Post, Comment

def naive_index_template(posts: list[Post]):
    posts_html = "\n".join([f"<li><a href=\"{ url_for('.post', post_id=post.post_id)  }\">{post.post_id} {post.title}</li>" for post in posts])
    body_html = f"""<h1>Posts</h1>
    <ul>{posts_html}</ul>"""
    return naive_html_base_template(body_html)

def naive_post_template(post: Post):
    body_html = f"""<h1>{post.title}</h1>
    {post.body}"""
    return naive_html_base_template(body_html)

def naive_comment_template(comment: Comment):
    return f"""comment: {comment}"""

def naive_html_base_template(body: str):
    return f"""<html>
<head>
    <title>really bad blog</title>
</head>
<body>
    {body}
</body>
</html>"""