import requests
import json

async def playerinfo(query):
     
    url = 'https://api.opendota.com/api/players/351193865'


    response = requests.request("GET", url)

    result =  response.json()

    json_object = json.dumps(result, indent=4)
    
    # Writing to sample.json
    with open("match_result.json", "w") as outfile:
        outfile.write(json_object)

    with open('match_result.json', 'r') as openfile:
    
        file_contents = openfile.read()
    
    parsed_json = json.loads(file_contents)
    personname = parsed_json["profile"]['personaname']
    print(personname)
