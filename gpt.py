import openai 
import os
import pathlib

def setup_gpt():
    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "gptkey.txt"), "r") as f:
        gptkey = f.readline()

    openai.api_key = gptkey

def get_compliment(msg, author):

    setup_gpt()
    print(msg)
    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "You are Willy. Give a passive aggressive response to the following message from "+ author.mention + ": " + msg}]
    )
    return response.choices[0].message.content
    
def get_insult(msg, author):

    setup_gpt()

    response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "You are Willy. Give an insult to "+ author.mention + " as a response to their message as follows: " + msg}]
    )
    return response.choices[0].message.content
