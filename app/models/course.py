# app/models/course.py

from sqlalchemy import Column, Integer, String
from app.database import Base

class Course(Base):
    __tablename__ = 'courses'  # The name of the table

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
