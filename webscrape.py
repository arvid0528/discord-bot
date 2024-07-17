import requests # type: ignore

def get_random_wiki_page_first_sentence():
        response = requests.get('https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=revisions|images&rvprop=content&grnlimit=10',
        params={
        'action': 'query',
        'format': 'json',
        'prop': 'extracts',
        'exintro': True,
        'explaintext': True,
        }
        ).json()
        wiki_text = next(iter(response['query']['pages'].values()))["extract"]
        
        return wiki_text[:wiki_text.find(".")+1]
      
if __name__ == "__main__":
        print(get_random_wiki_page_first_sentence())