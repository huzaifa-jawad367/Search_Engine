import json
import numpy as np
from nltk.stem import WordNetLemmatizer


def _search(list_of_words):
    results = {}
    for word in list_of_words:
        with open('Inverted_index.json', 'r') as fhand:
            x = fhand.read()
            inverted_index = json.loads(x)
            try:
                word_results = inverted_index[word]
                for url, info in word_results[1].items():
                    if url in results:
                        results[url][0] += info[0]
                        results[url][1] += info[1]
                    else:
                        results[url] = info
            except Exception as e:
                print(e)
                continue
    return len(results), results



with open('Inverted_index.json', 'r') as fhand:
    x = fhand.read()
    inverted_index = json.loads(x)

with open('length_of_docs.json', 'r') as fhand:
    x = fhand.read()
    length = json.loads(x)
   
lemmatizer = WordNetLemmatizer()
while True:
    query = input("Enter your query: ")
    results = _search(query.split(" "))
    page_score = {}
    for url, info in results[1].items():
        page_score[url] = info[0] * np.sum(1 - np.array(info[1]) / length[url])
    pages = sorted(page_score)
    for p in pages:
        print(p)
    break
