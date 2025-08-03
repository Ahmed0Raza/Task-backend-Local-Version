from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Make sure to import all models here
from .user import User
from .task import Task
