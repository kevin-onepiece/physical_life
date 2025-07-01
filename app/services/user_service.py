from ..repositories import user_repository

def register_user(username, email):
    # 可添加验证逻辑等
    return user_repository.create_user(username, email)
