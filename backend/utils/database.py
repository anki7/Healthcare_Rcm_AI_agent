from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
import os
import logging

logger = logging.getLogger(__name__)

# Get DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    logger.warning("DATABASE_URL not set, using SQLite for development")
    DATABASE_URL = "sqlite:///./healthcare.db"

# Fix for Render PostgreSQL (replace postgres:// with postgresql://)
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

logger.info(f"Using database: {DATABASE_URL.split('@')[0] if '@' in DATABASE_URL else DATABASE_URL}")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """Create all tables if they don't exist"""
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created/verified")
