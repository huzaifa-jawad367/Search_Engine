import json
import numpy as np
from nltk.stem import WordNetLemmatizer

with open('length_of_docs.json', 'r') as fhand:
    x = fhand.read()
    length = json.loads(x)

lemmatizer = WordNetLemmatizer()
while True:
    query = input("search: ")
    query = query.lower()
    query = lemmatizer.lemmatize(query)
    if query[0] in 'abcdefghijklmnopqrstuvwxyz':
        with open(f'Barrels/Inverted_index{query[0]}.json', 'r') as fhand:
            x = fhand.read()
            inverted_index = json.loads(x)
    else:
        with open(f'Barrels/Inverted_indexother.json', 'r') as fhand:
            x = fhand.read()
            inverted_index = json.loads(x)
    results = inverted_index[query]

    number_of_results = results[0]
    page_score = {}
    for url, info in zip(results[1].keys(), list(results[1].values())):
        page_score[url] = info[0]*np.sum(1 - np.array(info[1])/length[url])

    pages = sorted(page_score)
    for p in pages:
        print(p)

    break
