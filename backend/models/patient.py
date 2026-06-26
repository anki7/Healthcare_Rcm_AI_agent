from sqlalchemy import Column, Integer, String, DateTime, JSON, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String)
    conditions = Column(JSON, default=[])
    medications = Column(JSON, default=[])
    allergies = Column(JSON, default=[])
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Claim(Base):
    __tablename__ = "claims"
    
    id = Column(String, primary_key=True)
    patient_id = Column(String, nullable=False)
    procedure_codes = Column(JSON, default=[])
    diagnosis_codes = Column(JSON, default=[])
    amount = Column(Float, default=0.0)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Denial(Base):
    __tablename__ = "denials"
    
    id = Column(String, primary_key=True)
    patient_id = Column(String, nullable=False)
    claim_id = Column(String)
    carc_code = Column(String)
    description = Column(String)
    amount = Column(Float, default=0.0)
    priority = Column(String, default="MEDIUM")
    status = Column(String, default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
