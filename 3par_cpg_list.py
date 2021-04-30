from Storage_Credentials import * #3PAR Storage Credentials

import requests     #Module to handle HTTP Requests
from urllib3.exceptions import InsecureRequestWarning       

#To Suppress SSL Warning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Method Returns the Generates Session Key
def generate_key(storage_ip,user,pswd):
    
    #API URL to generate Session Key
    session_id_api = "https://"+ storage_ip + ":8080/api/v1/credentials"

    #Login Credentials for 3PAR
    login_cred = {'user':user,'password':pswd,'sessionType':1}
    
    #Session Key Generation for HTTP CURD Operations
    login = requests.post(session_id_api,json=login_cred,verify=False)
    session_id = login.json()["key"]

    #Return Generated Session Key
    return session_id


# Method Quesries the List of all CPGs and return JSON
def query_all_cpg(storage_ip,user,pswd):

    SessionKey = {"X-HP3PAR-WSAPI-SessionKey":generate_key(storage_ip,user,pswd)}
    
    #API URL Quesry List of CPGs
    api_url = "https://"+ storage_ip+ ":8080/api/v1/cpgs"    

    #Qery list of all CPGs
    data = requests.get(api_url,headers=SessionKey, verify = False)

    #Printing the HTTPS response StatusCode
    print(data.status_code)

    #List of CPGs in JSON format
    cpg_list = data.json()

    #Return List of CPGs as JSON
    return cpg_list

list_of_all_cpgs = query_all_cpg(storage_ip,username,password)
print(list_of_all_cpgs)







