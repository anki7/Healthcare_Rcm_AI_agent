from sqlalchemy import Column, Integer, String, DateTime, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(String, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    conditions = Column(JSON)
    medications = Column(JSON)
    allergies = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Claim(Base):
    __tablename__ = "claims"
    
    id = Column(String, primary_key=True)
    patient_id = Column(String)
    procedure_codes = Column(JSON)
    diagnosis_codes = Column(JSON)
    amount = Column(Float)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

class Denial(Base):
    __tablename__ = "denials"
    
    id = Column(String, primary_key=True)
    patient_id = Column(String)
    claim_id = Column(String)
    carc_code = Column(String)
    description = Column(String)
    amount = Column(Float)
    priority = Column(String)
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
