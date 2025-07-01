from ..models.user import User
from ..extensions import db

def get_user_by_id(user_id):
    # return User.query.get(user_id)
    return db.session.get(User, user_id)

def create_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user
