import requests
from requests.structures import CaseInsensitiveDict
import openai

QUERY_URL = "https://api.openai.com/v1/images/generations"
api_key = "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"

def generate_image(text):

    response = openai.Image.create(
    model = "image-alpha-001",
    prompt=text,
    n=1,
    size="1024x1024"
    )
    # try:
    #     resp = requests.post(QUERY_URL, headers=headers, json={"model": model_engine, "model_inputs": model_inputs})
    #     if resp.status_code != 200:
    #         raise ValueError("Failed to generate image")
    # except Exception as error:
    #             return 'Failed to generate image'
    return response['data'][0]['url']

