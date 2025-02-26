from ..extensions.database import database
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class User(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(255), nullable=False)
    conversations = relationship("Conversation", back_populates='conversation', uselist = False)
    created_at = database.Column(database.DateTime(timezone=True), server_default=func.now())
    updated_at = database.Column(database.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<Users {self.id}>'