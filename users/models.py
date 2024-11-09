# has sqlalchemy models
from sqlalchemy import Integer, Column, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base


collaborator_table = Table(
    "collaborators",
    Base.metadata,
    Column("project_id", ForeignKey("project.id")),
    Column("user_id", ForeignKey("users.id"))
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    email = Column(String(40), unique=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=True)
    full_name = Column(String(20), nullable=True)

    posts = relationship('Post', back_populates="user")
    projects = relationship("Project", back_populates="owner")

    def __str__(self):
        return f"User : {self.username}"


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="projects")
    collaborators = relationship("User", secondary=collaborator_table)

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id