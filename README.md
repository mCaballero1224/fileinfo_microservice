# fileinfo_microservice
A small python program that grabs data about a file and returns it as a JSON.

## Requesting Data

Requesting the JSON data can be done in one of two ways

### HTTP Request 

```
curl -o example_output.json -X POST http://localhost:5000/fileinfo -H "Content-Type: application/json" -d "{\"file_path\":\"/home/mcaballero/larbs.sh\"}"
```

### Programatically 
```
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
```

## UML Diagram
![UML Diagram for Client/Server communication](https://github.com/mCaballero1224/fileinfo_microservice/blob/main/UML.png)

## TODO

* Make microservice more configurable, allowing for singling out what info about the file is returned

* Add option for timestamp in case something more human-readable is needed' 
  
* The function only works with absolute file paths, figure out how to use relative paths

* Add functionality to send the file itself and extract info from it 
  
