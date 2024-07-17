from random import randint
import os
import pathlib

def get_random_line_in_file(filename):
    #TODO: Make this general
    adj_i = randint(0, 747)
    adj = ""
    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "negative_adjectives.txt"), "r") as f:
        lines = len(f.readlines())
        rand_index = randint(0, lines-1)
        for i, line in enumerate(f):
            if i == adj_i:
                adj = line
                break
            if i >= 747:
                break
    return adj[:-1]

def get_random_negative_adjective():
    adj_i = randint(0, 747)
    adj = ""
    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "negative_adjectives.txt"), "r") as f:
        lines = len(f.readlines())
        rand_index = randint(0, lines-1)
        for i, line in enumerate(f):
            if i == adj_i:
                adj = line
                break
            if i >= 747:
                break
    return adj[:-1]

def get_random_positive_adjective():
    adj_i = randint(0, 747)
    adj = ""
    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "positive_adjectives.txt"), "r") as f:
        for i, line in enumerate(f):
            if i == adj_i:
                adj = line
                break
            if i >= 747:
                break
    return adj[:-1]

def get_random_noun():
    noun_i = randint(0, 1410)
    noun = ""
    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "nouns.txt"), "r") as f:
            for i, line in enumerate(f):
                if i == noun_i:
                    noun = line
                    break
                if i >= 1410:
                    break
    return noun[:-1]

def generate_insult(member):
    vowels = "aeio"
    adj = get_random_negative_adjective()
    noun = get_random_noun()
    
    if adj[0].lower() in vowels:
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
        
    quote_i = randint(0, 165)

    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "quotes.txt"), "r") as f:
        for i, line in enumerate(f):
            if i == quote_i:
                quote = line
                break
            if i >= 165:
                break
    
    dash_i = quote.find('" -')

    quote = quote[:dash_i+1] + "\n" + quote[dash_i+1:]

    return quote