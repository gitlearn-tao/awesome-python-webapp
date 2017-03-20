# -*- coding=utf-8 -*-
import time;
from sqlalchemy import Column,String,create_engine;
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    #表的名字
    __tablename__='user'

    #表的结构
    id = Column(String(20),primary_key=True)
    email =Column(String(20))
    name = Column(String(20))

#初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://develop:swt240.48@10.1.251.244:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='5',name='Bob')
session.add(new_user)
session.commit()
session.close()





