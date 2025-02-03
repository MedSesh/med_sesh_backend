from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base is the parent class for all models
Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    major = Column(String)

    # Relationship: A student can have many courses
    courses = relationship("Course", back_populates="student")

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))

    # Relationship: A course belongs to a student
    student = relationship("Student", back_populates="courses")
