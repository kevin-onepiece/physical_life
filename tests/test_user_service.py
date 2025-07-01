from app.services import user_service

def test_register_user(db):
    user = user_service.register_user("charlie", "charlie@example.com")
    assert user.email == "charlie@example.com"
