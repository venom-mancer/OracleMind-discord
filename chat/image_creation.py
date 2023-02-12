import requests
from requests.structures import CaseInsensitiveDict
import openai

QUERY_URL = "https://api.openai.com/v1/images/generations"
api_key = "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"

def generate_image(text):

    
    try:
        response = openai.Image.create(
        model = "image-alpha-001",
        prompt=text,
        n=1,
        size="1024x1024"
        )
    except Exception as error:
                return 'Failed to generate image'
    return response['data'][0]['url']

