
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const analyzeResume = async (resumeFile, jobDescription) => {
  const formData = new FormData();
  formData.append('resume', resumeFile);
  formData.append('job_description', jobDescription);

  const response = await axios.post(`${API_URL}/analyze`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data;
};
