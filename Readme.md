## csp-demo

**this is purposefully bad code** to demonstrate [CSPs](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) by serving bad code. **do not use this code**, rather pick proper templating tools like [jinja2](https://jinja.palletsprojects.com/en/3.1.x/) or maybe even a full webframework like [django](https://www.djangoproject.com/).

## why then?

it's a sample app to demonstrate cross-site-scripting attacks and what [CSPs](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) can prevent. this was done as part of my talk on CSPs at the [devtreff](https://www.devtreff.com/).

## how to launch

do the following to run this.

```
# create a venv in ./venv
python -m venv ./venv

# activate the venv
source ./venv/bin/activate

# install dependencies
pip install -r requirements.txt

# fill database
flask --app bad_code init-database

# run flask
flask --app bad_code run --debug
```
