from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    text: str = None  # For pasted text

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

class ChatRequest(BaseModel):
    question: str
    document_text: str