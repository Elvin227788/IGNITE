import { useState } from 'react';
import UploadForm from './uploadform';
import Results from './result';
import Chatbot from './chatbot';

function App() {
  const [analysis, setAnalysis] = useState(null);
  const [documentText, setDocumentText] = useState('');

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold text-center mb-8">Legalese Translator</h1>
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <UploadForm setAnalysis={setAnalysis} setDocumentText={setDocumentText} />
          <Results analysis={analysis} />
        </div>
        <div>
          <Chatbot documentText={documentText} />
        </div>
      </div>
    </div>
  );
}

export default App;