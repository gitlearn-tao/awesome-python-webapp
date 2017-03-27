# -*- coding=utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine;
from model import User
#初始化数据库连接：
engine = create_engine('mysql+mysqlconnector://develop:broada123*#@10.1.251.61:3306/awesome')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='6',email='1204059425@qq.com',password='123',admin='root',name='root',image='123.png')
session.add(new_user)
session.commit()
session.close()