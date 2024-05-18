from random import randint

def generate_insult(member):
    vowels = "aeio"
    adj_i = randint(0, 747)
    noun_i = randint(0, 1410)
    adj = ""
    noun = ""
    with open("adjectives.txt", "r") as f:
        for i, line in enumerate(f):
            if i == adj_i:
                adj = line
                break
            if i >= 747:
                break

    with open("nouns.txt", "r") as f:
        for i, line in enumerate(f):
            if i == noun_i:
                noun = line
                break
            if i >= 1410:
                break
    
    if adj[0].lower() in vowels:
        msg = " is an "
    else:
        msg = " is a "
    
    msg += adj.lower()[:-1] + " " + noun.lower()
    print(member.mention + msg)
    
    return member.mention + msg

    