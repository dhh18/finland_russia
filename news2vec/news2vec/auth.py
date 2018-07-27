from functools import wraps
from flask import request, Response


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    secrets_file = 'secrets'
    with open(secrets_file, 'r') as f:
        content = f.readline().rstrip()
        type(content)
        print(content)

    valid_user, valid_password = tuple(content.split(':'))
    print(valid_user)
    print(valid_password)
    print(valid_password)
    return username == valid_user and password == valid_password


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated