def naive_index_template(posts):
    return f"""
<html>
<head>
    <title>really bad blog</title>  
</head>"""

def naive_post_template(title, body):
    body = f"""<h1>{title}</h1>
    <p>{body}</p>"""
    return naive_html_base_template(body)

def naive_comment_template(comment):
    return f"""comment: {comment}"""

def naive_html_base_template(body):
    return f"""<html>
<head>
    <title>really bad blog</title>
</head>
<body>
    {body}
</body>
</html>"""