from app.models.user import User
from app.repositories import user_repository

def test_create_user(db):
    user = user_repository.create_user("alice", "alice@example.com")
    assert user.id is not None
    assert user.username == "alice"

def test_get_user_by_id(db):
    user = user_repository.create_user("bob", "bob@example.com")
    fetched = user_repository.get_user_by_id(user.id)
    assert fetched.username == "bob"
