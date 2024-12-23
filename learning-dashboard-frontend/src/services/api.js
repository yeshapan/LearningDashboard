//service file
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api';

export const loginUser = async (email, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/login/`, { email, password });
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};

export const getCourses = async () => {
  try {
    const response = await axios.get(`${API_BASE_URL}/courses/`);
    return response.data;
  } catch (error) {
    throw error.response.data;
  }
};
