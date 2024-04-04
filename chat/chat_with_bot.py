#Deploying new question answer method

import json
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


model_name = "deepset/roberta-base-squad2"


with open('config.json') as user_file:
  file_contents = user_file.read()
parsed_json = json.loads(file_contents)

def talktobot(chat):

  nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)


  res = res["answer"]
  return res


model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

#