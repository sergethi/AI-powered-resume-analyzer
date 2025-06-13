import React from 'react';

const getScoreColor = (score) => {
  if (score >= 70) return 'bg-green-100 text-green-800';
  if (score >= 40) return 'bg-yellow-100 text-yellow-800';
  return 'bg-red-100 text-red-800';
};

const Results = ({ data }) => {
  const scoreColor = getScoreColor(data.match_score);

  return (
    <div className="p-4 rounded shadow-md bg-white max-w-xl mx-auto mt-6 space-y-4">
      <h3 className={`text-xl font-semibold p-3 rounded ${scoreColor}`}>
        Match Score: {data.match_score.toFixed(2)}%
      </h3>
      <p>
        <strong>✅ Matched Keywords:</strong>{' '}
        <span className="text-green-700">{data.matched_keywords.join(', ') || 'None'}</span>
      </p>
      <p>
        <strong>❌ Missing Keywords:</strong>{' '}
        <span className="text-red-700">{data.missing_keywords.join(', ') || 'None'}</span>
      </p>
    </div>
  );
};

export default Results;
