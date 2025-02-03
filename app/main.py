from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app.crud import course_crud, student_crud
from app.schemas import course, student

# Initialize FastAPI app
app = FastAPI()

# Database connection setup
DATABASE_URL = "sqlite:///./test.db"  # Use your SQLite database file
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Routes for course management
@app.post("/courses/", response_model=course.CourseCreate)
def create_course(course_data: course.CourseCreate, db: Session = Depends(get_db)):
    return course_crud.create_course(db=db, course_data=course_data)

@app.get("/courses/{course_id}", response_model=course.CourseCreate)
def get_course(course_id: int, db: Session = Depends(get_db)):
    return course_crud.get_course(db=db, course_id=course_id)

# Routes for student management (similarly for students)
@app.post("/students/", response_model=student.StudentCreate)
def create_student(student_data: student.StudentCreate, db: Session = Depends(get_db)):
    return student_crud.create_student(db=db, student_data=student_data)

@app.get("/students/{student_id}", response_model=student.StudentCreate)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return student_crud.get_student(db=db, student_id=student_id)
