import { cleanExcessSlashesInPath } from "@/utils";
import axios, { AxiosError, AxiosResponse } from "axios";

const baseUrl = 'http://127.0.0.1:8000';

/**
 * POST /cases
 * create a new case
 * @returns a string repr the case id
 */
export const xhrSubmitDashboard = async (payload: { medText: string; guideText: string }) => {
  try{
    const url = cleanExcessSlashesInPath(`${baseUrl}/cases`);
    const {data} = await axios.post(url, payload);
    console.log("Data:", payload);
    return data?.id || "";
  } catch(error: AxiosError | unknown){
    if(error instanceof AxiosError){
      const {response} = <AxiosError>error;
      const {status, data} = <AxiosResponse>response;
      throw {status, error: data};
    }
    else throw {status: -1, error};
  }
}

/**
 * GET /cases/<case-id>
 * get a case by case ID
 * @returns case data
 */
export const xhrReadCaseById = async (caseId: string) => {
  const url = cleanExcessSlashesInPath(`${baseUrl}/cases/${caseId.trim()}`);
  try{
    const {data} = await axios.get(url);
    return data;
  } catch(error: AxiosError | unknown){
    if(error instanceof AxiosError){
      const {response} = <AxiosError>error;
      const {status, data} = <AxiosResponse>response;
      throw {status, error: data};
    }
    else throw {status: -1, error};
  }
}