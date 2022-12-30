import json
import numpy as np
from nltk.stem import WordNetLemmatizer

with open('Inverted_index.json', 'r') as fhand:
    x = fhand.read()
    inverted_index = json.loads(x)

with open('length_of_docs.json', 'r') as fhand:
    x = fhand.read()
    length = json.dumps(x)

length_of_doc = 1000

lemmatizer = WordNetLemmatizer()
while True:
    query = input("search: ")
    query = lemmatizer.lemmatize(query)
    results = inverted_index[query]

    number_of_results = results[0]
    page_score = {}
    for url, info in zip(results[1].keys(), results[1].values()):
        page_score[url] = info[0]*np.sum(1 - np.array(info[1])/length[url])

    pages = sorted(page_score)
    for p in pages:
        print(p)

    break
