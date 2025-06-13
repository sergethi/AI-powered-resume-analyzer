
import React, { useState } from 'react';
import { analyzeResume } from '../api';
import Results from './Results';

const ResumeUpload = () => {
  const [resume, setResume] = useState(null);
  const [jobDesc, setJobDesc] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    const data = await analyzeResume(resume, jobDesc);
    setLoading(false);
    if (data.error) {
      setError("Error analyzing resume: " + data.error);
    } else {
      setResult(data);
    }
  };

  return (
    <div className="flex flex-col gap-4 bg-white p-6 rounded shadow-md">
      {error && <p className="text-red-500">{error}</p>}
      <form onSubmit={handleSubmit} className="flex flex-col gap-6 space-y-4">
        <div className="flex flex-col gap-2">
          <label className="text-sm font-medium">Upload Resume (PDF or Word):</label>
          <input type="file" accept=".pdf,.doc,.docx" onChange={(e) => setResume(e.target.files[0])} required />
        </div>
        
        <textarea
          rows="10"
          cols="50"
          placeholder="Paste job description here..."
          value={jobDesc}
          onChange={(e) => setJobDesc(e.target.value)}
          required
          className='border p-2 rounded w-full'
          style={{ resize: 'vertical' }}
        />
        <button type="submit" className='bg-blue-500 hover:bg-blue-600 text-white p-2 rounded'>{loading ? 'Analyzing...' : 'Analyze Resume'}</button>
      </form>
      {result && <Results data={result} />}
    </div>
  );
};

export default ResumeUpload;
