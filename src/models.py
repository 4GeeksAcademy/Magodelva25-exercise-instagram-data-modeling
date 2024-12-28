import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__='user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(32), nullable=False)
    name = Column(String(32))
    email = Column(String(32), nullable=False)
    pic_comments = Column(Integer, nullable=True)
    posts = Column(Integer, nullable=True)
    pictures = Column(Integer, nullable=True)
    pictures_likes = Column(Integer, ForeignKey('Pictures.Like'), nullable=True)
    posts_likes = Column(Integer, ForeignKey('Post.like'), nullable=True)

class Post(Base):
    __tablename__='post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    creation = Column(Integer, nullable=False)
    text_body = Column(String)
    likes = Column(Integer)
    post_counter = Column(Integer, ForeignKey('user.posts'))
    user = relationship(User)

class Pictures(Base):
    __tablename__='pictures'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    url = Column(String, nullable=False)
    likes = Column(Integer)
    comments = Column(Integer, ForeignKey('user.pic_comments'))
    pictures_counter = Column(Integer, ForeignKey('user.pictures'))
    user = relationship(User)

class Picture_comments(Base):
    __tablename__='picture-comments'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    picture_id = Column(Integer, ForeignKey('pictures.id'))
    txt_content = Column(String(300), nullable=False)
    likes = Column(Integer)
    user = relationship(User)
    pictures = relationship(Pictures)




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
