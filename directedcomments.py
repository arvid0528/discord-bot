
def contains_positive_adjective(msg):
    msg_as_word_list = msg.split(" ")

    with open("positive_adjectives.txt") as f:
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