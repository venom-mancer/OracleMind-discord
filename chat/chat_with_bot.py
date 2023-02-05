import openai

openai.api_key = "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"
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