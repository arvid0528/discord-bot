from random import randint
import os
import pathlib

def get_random_positive_adjective():
    adj_i = randint(0, 747)
    adj = ""
    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "adjectives.txt"), "r") as f:
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
    adj = get_random_positive_adjective()
    noun = get_random_noun()
    
    if adj[0].lower() in vowels:
        msg = " is an "
    else:
        msg = " is a "
    
    msg += adj.lower()[:-1] + " " + noun.lower()
    print(member.mention + msg)
    
    return member.mention + msg

    