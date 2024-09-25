import random
import os
import pathlib

def get_random_line_in_file(filename):
    path = os.path.join(pathlib.Path(__file__).parent.resolve(), filename)
    lines = list(open(path, "r", encoding="utf-8"))
    rand_line = random.choice(lines)
    return rand_line


def generate_insult(member):
    vowels = "aeio"
    adj = get_random_line_in_file("negative_adjectives.txt")
    noun = get_random_line_in_file("nouns.txt")
    
    if adj.lower() in vowels:
        msg = " is an "
    else:
        msg = " is a "
    
    msg += adj.lower() + " " + noun.lower()
    print(member.mention + msg)
    
    return member.mention + msg


def sentence_contains_word_in_file(filename, sentence):
    sentence_as_word_list = sentence.split(" ")

    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), filename)) as f:
        for i, line in enumerate(f):
            for word in sentence_as_word_list:
                if word.lower() == line[:-1].lower():
                    return True
        return False

def contains_positive_adjective(msg):
    msg_as_word_list = msg.split(" ")

    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "positive_adjectives.txt")) as f:
        for i, line in enumerate(f):
            for word in msg_as_word_list:
                if word.lower() == line[:-1].lower():
                    return True
        return False
    
def negations_amount(msg):
    msg_as_word_list = msg.split(" ")

    negations = [
        "not", "isnt", "isn't", "aint", "dont", "don't", "no"
    ]

    negations_amount = 0

    for word in msg_as_word_list:
        if word in negations:
            negations_amount += 1
    
    return negations_amount

def generate_quote():
        
    quote = get_random_line_in_file("quotes.txt")
    
    dash_i = quote.find('" -')

    quote = quote[:dash_i+1] + "\n" + quote[dash_i+1:]

    return quote