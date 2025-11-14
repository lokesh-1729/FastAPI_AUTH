from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey 

class Users(Base):
    __tablename__ = "users"
    id = Column[int](Integer, primary_key=True, index=True, autoincrement=True)
    username = Column[str](String, unique=True, index=True)
    password = Column[str](String)
    nick_name=Column[str](String)

