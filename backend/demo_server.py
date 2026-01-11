from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class RedFlag(BaseModel):
    clause: str
    reason: str

class Clause(BaseModel):
    title: str
    description: str

class AnalysisResponse(BaseModel):
    plain_translation: str
    red_flags: List[RedFlag]
    risk_score: int
    summary: str
    clauses: List[Clause]

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_document():
    return {
        "plain_translation": "This is a sample rental agreement. You agree to pay rent monthly, maintain the property, and follow all rules. The landlord can inspect the property with notice.",
        "red_flags": [
            {
                "clause": "Landlord may increase rent without notice",
                "reason": "This clause gives unlimited power to raise rent unexpectedly"
            },
            {
                "clause": "Tenant responsible for all repairs",
                "reason": "This shifts maintenance costs unfairly to the tenant"
            }
        ],
        "risk_score": 7,
        "summary": "Standard rental agreement with some concerning clauses about rent increases and repair responsibilities. Key obligations include monthly payments, property maintenance, and adherence to community rules.",
        "clauses": [
            {
                "title": "Payment Terms",
                "description": "Monthly rent due on the 1st of each month with late fees after 5 days"
            },
            {
                "title": "Maintenance Obligations",
                "description": "Tenant must keep property clean and report damages promptly"
            },
            {
                "title": "Termination Clause",
                "description": "Either party may terminate with 30 days written notice"
            }
        ]
    }

@app.post("/chat")
async def chat_with_document():
    return {"answer": "Based on the document, pets are allowed with a $200 deposit and landlord approval. Small dogs and cats are typically permitted."}

@app.get("/analyses")
async def get_analyses():
    return []

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
