import { useState } from 'react';
import { chatWithDocument } from './api';

function Chatbot({ documentText }) {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  const handleAsk = async () => {
    if (!documentText) {
      setAnswer('Please analyze a text document first (file uploads cannot be used for chat yet).');
      return;
    }
    if (!question.trim()) {
      setAnswer('Please enter a question.');
      return;
    }
    const result = await chatWithDocument(question, documentText);
    setAnswer(result.answer);
  };

  return (
    <div className="border p-4 rounded">
      <h3 className="font-semibold mb-2">Ask Questions</h3>
      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="e.g., Can I have a pet?"
        className="w-full p-2 border rounded mb-2"
      />
      <button onClick={handleAsk} className="bg-green-500 text-white px-4 py-2 rounded">Ask</button>
      {answer && <p className="mt-2">{answer}</p>}
    </div>
  );
}

export default Chatbot;