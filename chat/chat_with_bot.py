import openai
from configparser import ConfigParser


config = ConfigParser()
config.read('config.ini')

openai.api_key = config['credits']['open_ai_token']
openai.Model.list()


def talktobot(chat):


    response = openai.Completion.create(

        engine="text-davinci-003",
        prompt = "<|endoftext|>"+chat+"\n--\nLabel:",
        temperature=0.8,
        top_p=0.9,
        max_tokens=450,
    )

    output_label = response["choices"][0]["text"]

    return output_label