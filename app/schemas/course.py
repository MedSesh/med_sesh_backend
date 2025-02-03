from sqlalchemy.orm import Session
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate

# Create a new course
def create_course(db: Session, course: CourseCreate):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# Get a course by its ID
def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

# Get all courses
def get_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Course).offset(skip).limit(limit).all()

# Update a course
def update_course(db: Session, course_id: int, course: CourseUpdate):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course:
        for key, value in course.dict(exclude_unset=True).items():
            setattr(db_course, key, value)
        db.add(db_course)
        db.commit()
        db.refresh(db_course)
        return db_course
    return None

# Delete a course
def delete_course(db: Session, course_id: int):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course:
        db.delete(db_course)
        db.commit()
        return db_course
    return None
