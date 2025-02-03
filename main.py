from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Student
import crud

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint with a general welcome message
@app.get("/")
async def read_root():
    return {"message": "Welcome to MedSesh API! Providing medical and healthcare learning resources."}

# Endpoint for general medical content (can be expanded in the future)
@app.get("/medical-info/{topic_name}")
async def read_medical_info(topic_name: str):
    medical_info = {
        "insulin": "Insulin is a hormone that regulates blood glucose levels.",
        "cortisol": "Cortisol is a steroid hormone released in response to stress.",
        "hypertension": "Hypertension is high blood pressure, a common condition that can lead to heart disease and stroke."
    }
    return {"topic": topic_name, "info": medical_info.get(topic_name.lower(), "Information not available for this topic.")}

# Endpoint to create a new student
@app.post("/students/")
async def create_student(name: str, major: str, db: Session = Depends(get_db)):
    db_student = crud.create_student(db=db, name=name, major=major)
    return db_student

# Endpoint to read a student by ID
@app.get("/students/{student_id}")
async def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db=db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

# Endpoint to read all students
@app.get("/students/")
async def read_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db=db, skip=skip, limit=limit)
    return students

# Run the server when executing this file
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
