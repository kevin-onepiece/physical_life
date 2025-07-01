from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class School(Base):
    # 表的名字:
    __tablename__ = 'school'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    address = Column(String(50))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:12345678@localhost:3306/school')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)