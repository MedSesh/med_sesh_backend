# app/crud/course_crud.py

from sqlalchemy.orm import Session
from app.models.course import Course

def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()

def create_course(db: Session, name: str, description: str):
    db_course = Course(name=name, description=description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course
