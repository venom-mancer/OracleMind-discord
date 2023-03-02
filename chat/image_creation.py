import requests
from requests.structures import CaseInsensitiveDict
import openai
import json

with open('config.json') as user_file:
  file_contents = user_file.read()
parsed_json = json.loads(file_contents)

QUERY_URL = "https://api.openai.com/v1/images/generations"
api_key = parsed_json["open_ai_token"]

def generate_image(text):

    
    try:
        response = openai.Image.create(
        model = "image-alpha-001",
        prompt=text,
        n=1,
        size="1024x1024"
        )
    except Exception as error:
        return error.user_message,1
    return response['data'][0]['url'],2

