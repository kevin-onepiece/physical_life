import pytest
from app.extensions import db as _db
from app import create_app

# sqllite 测试
# @pytest.fixture(scope='session')
# def app():
#     app = create_app({
#         'TESTING': True,
#         'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
#         'SQLALCHEMY_TRACK_MODIFICATIONS': False
#     })
#
#     with app.app_context():
#         _db.create_all()
#         yield app
#         _db.drop_all()
#


@pytest.fixture(scope='session')
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'mysql+mysqlconnector://root:12345678@localhost:3306/jobs',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False
    })

    with app.app_context():
        _db.create_all()
        yield app
        _db.session.remove()
        # ❌ 不要 drop_all()，避免误删表！

@pytest.fixture(scope='function')
def db(app):
    yield _db
    _db.session.rollback()