#!/bin/bash

# Start script for IGNITE Legalese Translator
# This script starts both the backend and frontend servers

echo "Starting IGNITE Legalese Translator..."

# Check if backend dependencies are installed
if [ ! -d "backend/.venv" ] && [ ! -d "backend/venv" ]; then
    echo "Backend virtual environment not found. Creating one..."
    cd backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cd ..
fi

# Check if frontend dependencies are installed
if [ ! -d "frontend/node_modules" ]; then
    echo "Frontend dependencies not found. Installing..."
    cd frontend
    npm install
    cd ..
fi

# Check for .env file in backend
if [ ! -f "backend/.env" ]; then
    echo "Warning: backend/.env file not found. Please create it with your OPENAI_API_KEY"
    echo "You can copy .env.example: cp .env.example backend/.env"
fi

# Create uploads directory if it doesn't exist
mkdir -p backend/uploads

# Start backend
echo "Starting backend on http://localhost:8000..."
cd backend
source venv/bin/activate 2>/dev/null || source .venv/bin/activate
python main.py &
BACKEND_PID=$!
cd ..

# Wait a bit for backend to start
sleep 3

# Start frontend
echo "Starting frontend on http://localhost:3000..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "======================================"
echo "IGNITE Legalese Translator is running!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo "======================================"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for Ctrl+C
trap "kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; echo 'Servers stopped'; exit" INT
wait
