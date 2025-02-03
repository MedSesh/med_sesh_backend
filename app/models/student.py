# app/models/student.py

from sqlalchemy import Column, Integer, String
from app.database import Base

class Student(Base):
    __tablename__ = 'students'  # The name of the table

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
