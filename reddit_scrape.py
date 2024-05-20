import requests # type: ignore
import random

def roast():
    url = "https://reddit.com/r/roastme/comments.json?limit=200"
    data = requests.get(url, headers={"User-Agent": "/u/suudo http://compliment.b303.me (comments from gonewild)"}).json()
    comments = [a["data"]["body"] for a in data["data"]["children"]]
    return random.choice(comments)

def compliment():
    url = "https://reddit.com/r/freecompliments/comments.json?limit=200"
    data = requests.get(url, headers={"User-Agent": "/u/suudo http://compliment.b303.me (comments from gonewild)"}).json()
    comments = [a["data"]["body"] for a in data["data"]["children"]]
    return random.choice(comments)
