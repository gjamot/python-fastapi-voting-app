from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {"schema": "fastapi_voting_app"}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)