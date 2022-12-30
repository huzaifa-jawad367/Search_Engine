import json
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
  text = [lemmatizer.lemmatize(word) for word in text.split(' ')]
  return text

def preprocess_data(text):
    # Clean puntuation, urls, and so on
    text = clean_text(text)

    # Remove stopwords
    text = remove_stopwords(text)

    # Stemm all the words in the sentence
    text = lemm_data(text)
    
    return text

#load the english language stop words list
stop_words = stopwords.words('english')

#We can also add more stopwords according to our data/problem
more_stopwords = ['u', 'im', 'c', 'll', "’", '‘', '”', '“']
stop_words = stop_words + more_stopwords

lemmatizer = WordNetLemmatizer() # defining lemmitizer object
# vectorizer = CountVectorizer()

listOfJson = os.listdir('articles_dataset\json\\nela-gt-2021\\newsdata\\train')

lenOfDocs = {}

for fil in listOfJson:
    with open(f'articles_dataset\json\\nela-gt-2021\\newsdata\\train\{fil}', 'r') as fhand:
        listOfArticles = fhand.read()
        listOfArticles = json.loads(listOfArticles)
        for article in listOfArticles:
            corpus = preprocess_data(article['content'])
            lenOfDocs[article['url']] = len(corpus)


x = json.dumps(lenOfDocs)
with open('length_of_docs.json', 'w') as f:
    f.write(x)