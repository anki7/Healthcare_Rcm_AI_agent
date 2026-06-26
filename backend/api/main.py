from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import uvicorn
import logging
from datetime import datetime
import random
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.database import get_db, Base, engine
from models.patient import Patient, Claim, Denial
from mcp_servers.fhir_server import FHIRMCPServer
from mcp_servers.coding_server import CodingMCPServer
from mcp_servers.denial_server import DenialMCPServer
from agents.revenue_optimizer import RevenueOptimizer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Healthcare RCM AI Agent",
    description="Advanced Revenue Cycle Management System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://*.onrender.com",
        "https://*.vercel.app",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fhir_server = FHIRMCPServer()
coding_server = CodingMCPServer()
denial_server = DenialMCPServer()
revenue_optimizer = RevenueOptimizer()

MOCK_PATIENTS = [
    {"id": "P0001", "name": "John Doe", "age": 65, "gender": "M", 
     "conditions": ["Type 2 Diabetes", "Hypertension"], 
     "medications": ["Metformin", "Lisinopril"], "allergies": ["Penicillin"]},
    {"id": "P0002", "name": "Jane Smith", "age": 45, "gender": "F", 
     "conditions": ["Asthma"], "medications": ["Albuterol"], "allergies": ["Sulfa"]},
]

MOCK_DENIALS = [
    {"id": "DNL0001", "patient_id": "P0001", "claim_id": "CLM10001", 
     "carc_code": "CO-11", "description": "Diagnosis inconsistent with procedure", 
     "amount": 250.00, "priority": "HIGH", "status": "open"},
    {"id": "DNL0002", "patient_id": "P0002", "claim_id": "CLM10002", 
     "carc_code": "CO-4", "description": "Procedure code inconsistent with modifier", 
     "amount": 150.00, "priority": "MEDIUM", "status": "open"},
]

@app.get("/")
async def root():
    return {"status": "healthy", "message": "Healthcare RCM AI Agent", "timestamp": datetime.now().isoformat()}

@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    # Test database connection
    try:
        db.execute("SELECT 1")
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "services": {
            "fhir_server": "running",
            "coding_server": "running",
            "denial_server": "running"
        },
        "database": db_status
    }

@app.get("/api/patients")
async def get_patients():
    return {"patients": MOCK_PATIENTS, "count": len(MOCK_PATIENTS)}

@app.get("/api/patients/{patient_id}")
async def get_patient(patient_id: str):
    patient = next((p for p in MOCK_PATIENTS if p["id"] == patient_id), None)
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient {patient_id} not found")
    return {"patient": patient, "timestamp": datetime.now().isoformat()}

@app.get("/api/denials")
async def get_denials(limit: int = 50):
    return {"denials": MOCK_DENIALS[:limit], "count": len(MOCK_DENIALS)}

@app.post("/api/claims/process")
async def process_claim(claim_data: dict):
    claim_id = f"CLM{random.randint(10000, 99999)}"
    risk_score = random.randint(10, 90)
    return {
        "claim_id": claim_id,
        "status": "submitted" if risk_score < 70 else "flagged_for_review",
        "risk_score": risk_score,
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/analytics/revenue")
async def get_revenue_analytics():
    return {
        "total_claims": 1247,
        "total_revenue": 385290.50,
        "denial_rate": 8.2,
        "days_in_ar": 28,
        "ai_savings": {"auto_corrected": 134, "appeals_won": 87, "estimated_savings": 45230.00}
    }

if __name__ == "__main__":
    print("=" * 50)
    print("🏥 Healthcare RCM AI Agent")
    print("=" * 50)
    print("🚀 Starting server at http://0.0.0.0:8000")
    print("📚 API Docs: http://0.0.0.0:8000/docs")
    print("=" * 50)
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=False)
