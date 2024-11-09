from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from users.models import User


class Post(Base):
    __tablename__ = "user_posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(40))
    posted_date = Column(Date)
    content = Column(Text)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship('User', back_populates="posts")
