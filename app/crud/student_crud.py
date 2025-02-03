# app/crud/student_crud.py

from sqlalchemy.orm import Session
from app.models.student import Student

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

def create_student(db: Session, name: str, email: str):
    db_student = Student(name=name, email=email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
