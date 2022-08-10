from flask import Flask
from flask_httpauth import HTTPBasicAuth

from lib import users

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    for user in users:
        if user.username == username:
            return user.password
    return None


@app.route("/")
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


if __name__ == "__main__":
    app.run()
