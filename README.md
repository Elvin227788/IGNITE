# AMD HACKATHON - Legalese Translator
REPO OF 404 FOUND TEAM FOR AMD HACKATHON

## Overview
A web application that translates complex legal documents into plain English, identifies red flags, and provides an AI chatbot for questions.

## Tech Stack
- **Backend**: FastAPI, Python, SQLAlchemy, LangChain, OpenAI
- **Frontend**: React, Vite, Tailwind CSS
- **OCR**: Tesseract, pdf2image

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- OpenAI API Key

### Backend Setup
1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file in the root directory:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```

4. Start the backend server:
   ```bash
   python main.py
   ```
   Backend will run on http://localhost:8000

### Frontend Setup
1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   Frontend will run on http://localhost:3000

## Features
- 📄 Upload PDF documents or paste text
- 🔍 Plain English translation of legal jargon
- 🚩 Red flag detection for risky clauses
- 📊 Risk scoring (1-10)
- 📝 Clause-by-clause breakdown
- 💬 AI chatbot for document questions
- 💾 Analysis history storage

## Usage
1. Upload a PDF or paste legal text
2. Click "Analyze" to process the document
3. Review the plain English translation
4. Check red flags and risk score
5. Ask questions using the chatbot

## Team
404 FOUND - AMD 
Hackathon
