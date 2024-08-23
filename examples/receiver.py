import requests
import json

def get_file_info(url, file_path):
    # setup request msg
    request_dict = {'file_path': file_path}
    
    # send request and save response 
    response = requests.post(url, json=request_dict)
    
    # if the response is OK
    if response.status_code == 200:
        # Print the JSON response
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error retrieving file info. Status: {response.status_code}\nResponse: {response.text}")

if __name__ == "__main__":
    server_url = "http://localhost:5000/fileinfo"

    file_path = "C:/Users/Max/Downloads/test2(1).csv"

    # request file and print the JSON response
    get_file_info(server_url, file_path)
