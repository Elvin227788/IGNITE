import axios from 'axios';

const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export const analyzeDocument = async (data) => {
  const response = await axios.post(`${API_BASE}/analyze`, data, {
    headers: {
      'Content-Type': data instanceof FormData ? 'multipart/form-data' : 'application/json'
    }
  });
  return response.data;
};

export const chatWithDocument = async (question, documentText) => {
  const response = await axios.post(`${API_BASE}/chat`, { question, documentText });
  return response.data;
};

export const getAnalyses = async () => {
  const response = await axios.get(`${API_BASE}/analyses`);
  return response.data;
};