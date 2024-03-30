from bad_code.bad_blog.db import get_db, Post

from .naive_templating import naive_post_template, naive_index_template
from .. import blueprint


@blueprint.route('/')
def index():
    db = get_db()
    posts = [ Post(post_id=row['post_id'],title=row['title'], body=row['body'], comments=[]) for row in db.execute('SELECT * FROM post').fetchall()]
    return naive_index_template(posts)

@blueprint.route('/<int:post_id>', methods=('GET',))
def post(post_id: int):
    db = get_db()
    post_row = db.execute(
        'SELECT * FROM post WHERE post_id = ?', (post_id,)
    ).fetchone()
    post = Post(post_id=post_row['post_id'] ,title=post_row['title'], body=post_row['body'], comments=[])
    return naive_post_template(post)

@blueprint.route('/<int:post_id>/add-comment', methods=('POST',))
def add_comment(post_id):
    return f'we just added a comment! {post_id}'