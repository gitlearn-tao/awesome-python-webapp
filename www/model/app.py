# -*- coding=utf-8 -*-

from flask import Flask,request,render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine;
from model import User

app = Flask(__name__)

engine = create_engine('mysql+mysqlconnector://develop:broada123*#@10.1.251.61:3306/awesome')
DBSession = sessionmaker(bind=engine)

session = DBSession()

@app.route('/',methods=['GET'])
def index():
    users = session.query(User.name).all()
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test users - Awesome Python Webapp</title>
</head>
<body>
    <h1>All users</h1>
    {% for u in users %}
    <p>{{ u.name }} / {{ u.email }}</p>
    {% endfor %}
</body>
</html>'''

if __name__ == '__main__':
    app.run()




