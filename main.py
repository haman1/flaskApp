from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)


engine = create_engine ('postgresql://postgres:matigari@localhost/flaskApp')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()




db = SQLAlchemy()

class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))



Base.metadata.create_all(engine)

@app.route('/')
def index():
   return "hey Ninjaz!!!"





if __name__ == '__main__':
    app.run()
