from flask import Flask
from flask_httpauth import HTTPBasicAuth

from lib import users

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    table = {}
    for user in users:
        table[user.username] = user.password
    if username in table:
        return table.get(username)
    return None


@app.route("/")
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


if __name__ == "__main__":
    app.run()
