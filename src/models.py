from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    __tablename__="user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)   

    #relationships
    favorites: Mapped[List["Favorites"]] = relationship(back_populates="user")


class Favorites(db.Model):
    __tablename__="favorites"

    id: Mapped[int] = mapped_column(primary_key=True)

    #foreingkeys
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    #relationships
    user: Mapped["User"] = relationship(back_populates="favorites")
    favorites_planet: Mapped[List["FavoritePlanet"]] = relationship(back_populates="favorites")
    favorites_character: Mapped[List["FavoriteCharacter"]] = relationship(back_populates="favorites")
    favorites_starship: Mapped[List["FavoriteStarship"]] = relationship(back_populates="favorites")     


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    climate: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    diametre: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)


class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    lastname: Mapped[str] = mapped_column(String(90), unique=True, nullable=False)
    height: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    original_planet: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
       

    
class Starship(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    crew: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
       
