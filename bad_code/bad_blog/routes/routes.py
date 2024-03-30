from bad_code.bad_blog.db import get_db

from .naive_templating import naive_post_template
from .. import blueprint


@blueprint.route('/')
def index():
    db = get_db()
    post_count = db.execute('SELECT * FROM post').fetchall()
    print('*'*50)
    print(post_count[0]['title'])
    return f"{post_count}"

@blueprint.route('/<int:post_id>', methods=('GET',))
def post(post_id: int):
    db = get_db()
    post = db.execute(
        'SELECT * FROM post WHERE post_id = ?', (post_id,)
    ).fetchone()
    return naive_post_template(post['title'], post['body'])

@blueprint.route('/<int:post_id>/add-comment', methods=('POST',))
def add_comment(post_id):
    return f'we just added a comment! {post_id}'