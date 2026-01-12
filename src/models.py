from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)    

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,            
        }
    
class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
       

    def serialize(self):
        return {
            "id": self.id,
            "username": self.name,            
        }

class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    original_planet: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
       

    def serialize(self):
        return {
            "id": self.id,
            "username": self.name,            
        }
    
class Starships(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
       

    def serialize(self):
        return {
            "id": self.id,
            "username": self.name,            
        }    
