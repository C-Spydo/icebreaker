from ..extensions.database import database
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    fullname = database.Column(database.String(255), nullable=False)
    email = database.Column(database.String(255), nullable=False, unique=True)
    google_id = database.Column(database.String(255), nullable=False)
    created_at = database.Column(database.DateTime(timezone=True), server_default=func.now())
    updated_at = database.Column(database.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<User {self.id}>'
    
    def  serialize(self):
        return {
            'fullname': self.fullname,
            'email': self.email
        }