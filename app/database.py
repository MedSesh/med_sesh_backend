# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (adjust according to your actual database configuration)
DATABASE_URL = "sqlite:///./test.db"  # For SQLite, adjust for PostgreSQL/MySQL as needed

# Set up the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # SQLite-specific option

# Base class for models
Base = declarative_base()

# Session local to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)