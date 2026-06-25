class DenialMCPServer:
    def __init__(self):
        pass
    
    async def get_worklist(self, limit: int = 50, status: str = "open"):
        return []
    
    async def analyze_denial(self, denial_id: str, carc_code: str = "CO-11"):
        return {"denial_id": denial_id, "category": "Medical Necessity", "fixes": ["Review documentation"]}
    
    async def draft_appeal(self, denial: dict):
        return "Appeal letter content"
