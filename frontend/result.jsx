function Results({ analysis }) {
  if (!analysis) return <p>Upload or paste a document to analyze.</p>;

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Analysis Results</h2>
      <p><strong>Risk Score:</strong> {analysis.risk_score}/10</p>
      <h3>Plain English Translation:</h3>
      <p className="mb-4">{analysis.plain_translation}</p>
      <h3>Red Flags:</h3>
      <ul className="mb-4">
        {analysis.red_flags.map((flag, i) => (
          <li key={i} className="text-red-600">{flag.clause}: {flag.reason}</li>
        ))}
      </ul>
      <h3>Summary of Obligations:</h3>
      <p className="mb-4">{analysis.summary}</p>
      <h3>Clause Breakdown:</h3>
      <ul>
        {analysis.clauses.map((clause, i) => (
          <li key={i}><strong>{clause.title}:</strong> {clause.description}</li>
        ))}
      </ul>
    </div>
  );
}

export default Results;