class CodingMCPServer:
    def __init__(self):
        pass
    
    async def code_lookup(self, code: str, code_type: str = "auto"):
        return {"code": code, "code_type": code_type, "description": "Sample code"}
    
    async def get_reimbursement(self, code: str):
        return {"code": code, "medicare_payment": 100.00}
