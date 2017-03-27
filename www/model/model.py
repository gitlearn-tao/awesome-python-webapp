# -*- coding=utf-8 -*-
import time;
from sqlalchemy import Column,String,Boolean,Float;
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    #表的名字
    __tablename__='users'

    #表的结构
    id = Column(String(20),primary_key=True)
    email =Column(String(20))
    password = Column(String(20))
    admin = Column(Boolean)
    name  = Column(String(50))
    image = Column(String(500))
    created_at = Column(Float,default=time.time())







