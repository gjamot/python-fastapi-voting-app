from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum

Base = declarative_base()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class PostInfo(BaseModel):
    title: str
    
class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {"schema": "fastapi_voting_app"}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)