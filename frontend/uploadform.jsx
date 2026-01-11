import { useState } from 'react';
import { analyzeDocument } from './api';

function UploadForm({ setAnalysis, setDocumentText }) {
  const [text, setText] = useState('');
  const [file, setFile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    let result;
    if (file) {
      // Send as multipart/form-data for file upload
      const formData = new FormData();
      formData.append('file', file);
      result = await analyzeDocument(formData);
      setDocumentText('');  // File text will be extracted by backend
    } else if (text) {
      // Send as JSON for text input
      result = await analyzeDocument({ text });
      setDocumentText(text);
    } else {
      alert('Please provide text or upload a file');
      return;
    }
    
    setAnalysis(result);
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