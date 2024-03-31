from flask import url_for

from bad_code.bad_blog.db import Comment, Post


def naive_index_template(posts: list[Post]):
    posts_html = "\n".join(
        [
            f"<li><a href=\"{ url_for('.post', post_id=post.post_id)  }\">{post.post_id} {post.title}</li>"
            for post in posts
        ]
    )
    body_html = f"""<h1 class="display-4">Posts</h1>
    <ul>{posts_html}</ul>"""
    return naive_html_base_template(body_html)


def naive_post_template(post: Post):
    comments_html = "\n".join([naive_comment_template(comment) for comment in post.comments])
    body_html = f"""<h1 class="display-4">{post.title}</h1>
    <img class="img-fluid rounded" src="https://picsum.photos/800/600">
    {post.body}
    <hr>
    <h3>Leave a comment</h3>
    {naive_comment_form(post)}
    <hr>
    <h3>Comments</h3>
    {comments_html}
"""
    return naive_html_base_template(body_html)


def naive_comment_form(post: Post):
    return f"""<form method="post" action="/{post.post_id}/add-comment">
    <label class="form-label" for="title">Title</label><br>
    <input class="form-control" type="text" name="title" placeholder="Title"><br>
    <label class="form-label" for="body">Your comment</label><br>
    <textarea class="form-control" name="body" placeholder="Tell us what you like"></textarea><br>
    <input class="btn btn-primary" type="submit" value="Submit">
</form>"""


def naive_comment_template(comment: Comment):
    comment_html = f"""<h4>{comment.title}</h4>
    <p>{comment.body}</p>
"""
    return comment_html


def naive_html_base_template(body: str):
    more_meta = ""  # _csp_meta_tag()

    return f"""<!doctype html>
<html lang="en">
<head>
    <title>really bad blog</title>
    {more_meta}
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body class="bg-body-tertiary">
    <nav class="navbar bg-dark border-bottom border-body" data-bs-theme="dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">Really bad blog</a>
    </div>
    </nav>
    <div class="container-fluid">
        <div class="container">
        {body}
        </div>
    </div>
    <footer class="navbar bg-dark fixed-bottom" data-bs-theme="dark">
        <div class="navbar-nav"><span class="navbar-text">© 2024 Johnny Gringo<span></div>
    </footer>
</body>
</html>"""


def _csp_meta_tag():
    return '<meta http-equiv="Content-Security-Policy" content="default-src \'self\'; style-src *;"/>'
