from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import json
from database import SessionLocal, Analysis
from models import AnalyzeRequest, AnalysisResponse, ChatRequest
from ai_processor import process_document, answer_question
from ocr import extract_text_from_pdf

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_document(request: AnalyzeRequest = None, file: UploadFile = File(None)):
    text = ""
    if file:
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        else:
            raise HTTPException(status_code=400, detail="Only PDF uploads supported")
    elif request and request.text:
        text = request.text
    else:
        raise HTTPException(status_code=400, detail="Provide text or file")

    result = process_document(text)
    
    # Save to DB
    db = SessionLocal()
    analysis = Analysis(
        original_text=text,
        plain_translation=result["plain_translation"],
        red_flags=json.dumps(result["red_flags"]),
        risk_score=result["risk_score"],
        summary=result["summary"],
        clauses=json.dumps(result["clauses"])
    )
    db.add(analysis)
    db.commit()
    db.refresh(analysis)
    db.close()
    
    return result

@app.post("/chat")
async def chat_with_document(request: ChatRequest):
    answer = answer_question(request.question, request.document_text)
    return {"answer": answer}

@app.get("/analyses")
async def get_analyses():
    db = SessionLocal()
    analyses = db.query(Analysis).all()
    db.close()
    return [
        {
            "id": a.id,
            "plain_translation": a.plain_translation,
            "red_flags": json.loads(a.red_flags),
            "risk_score": a.risk_score,
            "summary": a.summary,
            "clauses": json.loads(a.clauses)
        } for a in analyses
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)