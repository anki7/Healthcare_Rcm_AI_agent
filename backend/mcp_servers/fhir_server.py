class FHIRMCPServer:
    def __init__(self):
        pass
    
    async def get_patient_snapshot(self, patient_id: str):
        return {"id": patient_id, "name": "Test Patient", "status": "active"}
    
    async def calculate_acuity(self, observations: list):
        return {"acuity": "STABLE", "flags": [], "confidence": 100}
    
    async def calculate_raf_score(self, conditions: list):
        return {"total_raf": 1.0, "hcc_codes": [], "base_raf": 1.0}
