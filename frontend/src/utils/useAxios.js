import axios from "axios";
import { setAuthUser, getRefreshedToken, isAccessTokenExpired } from "./auth";
import Cookies from "js-cookie";
import { API_BASE_URL } from "./constants";

const useAxios = () => {
    const accessToken = Cookies.get("access_token");
    const refreshToken = Cookies.get("refresh_token");

    const axiosInstance = axios.create({
        baseURL: API_BASE_URL,
        headers: { Authorization: `Bearer ${accessToken}` },
    });

    axiosInstance.interceptors.request.use(async (req) => {
        if (!isAccessTokenExpired(accessToken)) {
            // Pass the token here
            return req;
        }

        console.log(accessToken);
        console.log(refreshToken);

        const response = await getRefreshedToken(refreshToken);
        console.log("response.data ====", response?.data);
        console.log("response.data?.access ====", response?.data?.access);

        setAuthUser(response.data?.access, response.data?.refresh);
        req.headers.Authorization = `Bearer ${response.data?.access}`;
        return req;
    });

    return axiosInstance;
};

export default useAxios;

