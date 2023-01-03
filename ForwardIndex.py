import pandas as pd
import json
import time
import re
import os
import string
import nltk
import numpy as np
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
   
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

def clean_text(text):
    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    #Lower Case
    text = str(text).lower()

    #Remove links starting with https/www
    text = re.sub('https?://\S+|www\.\S+', '', text)

    #Remove punctuation
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)

    #Remove new line character
    text = re.sub('\n', '', text)

    #Remove words containing numbers
    text = re.sub('\w*\d\w*', '', text)

    return text

#Define a function to remove the stop words from the corpus
def remove_stopwords(text):
    text = ' '.join(word for word in text.split(' ') if word not in stop_words)
    return text

def lemm_data(text):
  text = ' '.join([lemmatizer.lemmatize(word) for word in text.split(' ')])
  return text

def preprocess_data(text):
    # Clean puntuation, urls, and so on
    text = clean_text(text)

    # Remove stopwords
    text = remove_stopwords(text)

    # Stemm all the words in the sentence
    text = lemm_data(text)
    
    return text

def forward_Indexing(path = 'articles_dataset\json\\nela-gt-2021\\newsdata\\train\\'):
    # Loading Data
    listOfArticles = []
    listOfJson = os.listdir(path)

    start_time = time.time()

    forward_Barrel = {}
    for fil in listOfJson:
        fhand = open(path + fil, 'r')
        x = fhand.read()

        listOfArticles = json.loads(x)

        fhand.close()

        for article in listOfArticles:

            # corpus = [preprocess_data(article['content']) for article in listOfArticles]
            clean_title = [preprocess_data(article['title'])]

            # corpus = [clean_title[0]+preprocess_data(listOfArticles[0]['content'])]  -- dont need to add clean text to the corpus just yet
            corpus = [preprocess_data(article['content'])]
            clean_title = [ct.split() for ct in clean_title]
            # print(clean_title)
            try:
                X = vectorizer.fit_transform(corpus)
            except:
                continue
            word_bank = vectorizer.get_feature_names_out()

            X = X.toarray()
            # print(X.shape)


            forward_index = {}
            for i,j in zip(word_bank, X[0]):
                forward_index[i] = [j, []]

            for word, pos in zip(corpus[0].split(), range(1,len(corpus[0].split())+1)):
                try:
                    forward_index[word][1].append(pos)
                except:
                    try:
                        word = word.strip('’') # "’", '‘', '”', '“'
                        word = word.strip('‘')
                        word = word.strip('”')
                        word = word.strip('“')
                        forward_index[word][1].append(pos)
                    except:
                        continue
                


            for title in clean_title[0]:
                try:
                    forward_index[title][1].insert(0, 0)
                    forward_index[title][0] += 1
                except:
                    forward_index[title] = [1, [0]]

            # to find the position we will loop through the content until we find the word the number of times it occurs
            # print(forward_index)

            # some words' position failed to be added to the to the index so we assigned a value of -1 for them; -1 indicating that position is unknown
            for w in forward_index.keys():
                if forward_index[w][0] > len(forward_index[w][1]):
                    forward_index[w][1] += [-1] * (forward_index[w][0]-len(forward_index[w][1]))

            forward_Barrel[article['url']] = forward_index

    print('time taken for forward indexing:', time.time() - start_time)

    # f_index = json.dumps(forward_Barrel, cls=NpEncoder)

    # with open('forward_index.json', 'w') as fhand:
    #     fhand.write(f_index)

    print("Number of articles in the forward index:", len(forward_Barrel.keys()))

    return forward_Barrel

#load the english language stop words list
stop_words = stopwords.words('english')

#We can also add more stopwords according to our data/problem
more_stopwords = ['u', 'im', 'c', 'll', "’", '‘', '”', '“']
stop_words = stop_words + more_stopwords

lemmatizer = WordNetLemmatizer() # defining lemmitizer object 
vectorizer = CountVectorizer()
# print(forward_Indexing())