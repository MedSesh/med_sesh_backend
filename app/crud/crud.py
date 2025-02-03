from sqlalchemy.orm import Session
from app.models.models import Student, Course

# Function to create a new student
def create_student(db: Session, name: str, major: str):
    db_student = Student(name=name, major=major)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

# Function to create a new course for a student
def create_course(db: Session, student_id: int, course_name: str):
    db_course = Course(name=course_name, student_id=student_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# Function to get a student by ID
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

# Function to get all students with pagination
def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

# Function to get all courses for a student
def get_courses_for_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        return student.courses  # This uses the relationship to get all courses
    return None

# Function to get all courses
def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()
