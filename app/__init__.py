from flask import Flask
from .config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from .extensions import db

def create_app(test_config=None):
    app = Flask(__name__)

    # 先加载默认配置
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    # 如果有测试配置，覆盖默认配置
    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    with app.app_context():
        from .models import user  # 导入模型以创建表
        db.create_all()

    return app
