import requests
import json 


with open('config.json') as user_file:
  file_contents = user_file.read()
parsed_json = json.loads(file_contents)

rapidapi_key = parsed_json["X-RapidAPI-Key"]

url = "https://chat-gpt26.p.rapidapi.com/"
def talktobot(chat):
      
    payload = {
      "model": "gpt-4-1106-preview",
      "messages": [
        {
          "role": "user",
          "content": chat,
        }
      ]
    }
    headers = {
      "content-type": "application/json",
      "Content-Type": "application/json",
      "X-RapidAPI-Key": "{}".format(rapidapi_key),
      "X-RapidAPI-Host": "chat-gpt26.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    parsed_json = json.loads(response.text)

    return parsed_json["choices"][0]["message"]["content"]