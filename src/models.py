import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    correo = Column(String(50), nullable=False)
    contrasena = Column(String(50), nullable=False)
    fecha_registro = Column(String(50), nullable=False)
    
    favorite_planet = relationship("Favorite_Planet", back_populates="user")
    favorite_character = relationship("Favorite_Character", back_populates="user")


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    poblacion = Column(String(50), nullable=False)

   


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    genero = Column(String(50), nullable=False)
    altura = Column(String(40), nullable=False)
    peso = Column(String(40), nullable=False)



class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    
    user = relationship(User, back_populates="favorite_planet")
    

class Favorite_Character(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User, back_populates="favorite_character")    
    
       
 # __table_args__ = (CheckConstraint(id <= 5, name='check_max_planets'),


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
