import { useState } from 'react';
import { analyzeDocument } from '../api';

function UploadForm({ setAnalysis, setDocumentText }) {
  const [text, setText] = useState('');
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    if (file) formData.append('file', file);
    else formData.append('text', text);
    
    const result = await analyzeDocument(formData);
    setAnalysis(result);
    setDocumentText(text || '');  // For chat
  };

  return (
    <form onSubmit={handleSubmit} className="mb-8">
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste legal text here..."
        className="w-full p-2 border rounded mb-4"
        rows={6}
      />
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">Analyze</button>
    </form>
  );
}

export default UploadForm;