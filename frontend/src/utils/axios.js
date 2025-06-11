import axios from "axios";
import { API_BASE_URL } from "./constants";


// Create an Axios instance with default settings
const apiInstance = axios.create({
    baseURL: API_BASE_URL,
    timeout: 10000,
    headers: {
        "Content-Type": "application/json",
    },
});

export default apiInstance;