
from . import api
from application.models.user import User

@api.route("/users")
def hello_users():
    return "users"