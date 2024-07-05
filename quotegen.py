from random import randint
import os
import pathlib

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

        