import pandas as pd
import json
import time
import re
import os
import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
   

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


# Loading Data
listOfArticles = []
listOfJson = os.listdir('articles_dataset\json\\nela-gt-2021\\newsdata\\train')

# for fil in listOfJson:
#     fhand = open(f'articles_dataset\json\\nela-gt-2021\\newsdata\\train\\{fil}', 'r')
#     x = fhand.read()

#     x = json.loads(x)
#     listOfArticles = listOfArticles + x
#     fhand.close()
fil = listOfJson[0]

fhand = open(f'articles_dataset\json\\nela-gt-2021\\newsdata\\train\\{fil}', 'r')
x = fhand.read()

x = json.loads(x)
listOfArticles = listOfArticles + x
fhand.close()

start_time = time.time()

#load the english language stop words list
stop_words = stopwords.words('english')

#We can also add more stopwords according to our data/problem
more_stopwords = ['u', 'im', 'c', 'll', "’", '‘', '”', '“']
stop_words = stop_words + more_stopwords

# # Lemmitization
lemmatizer = WordNetLemmatizer() # defining lemmitizer object

# corpus = [preprocess_data(article['content']) for article in listOfArticles]
clean_title = [preprocess_data(listOfArticles[0]['title'])]

# length_of_title = [len(clean_title[0])]
corpus = [clean_title[0]+preprocess_data(listOfArticles[0]['content'])]
clean_title = [ct.split() for ct in clean_title]
# print(clean_title)
# print(corpus[0], '\n')

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(corpus)
word_bank = vectorizer.get_feature_names_out()

X = X.toarray()
print(X.shape)


number_of_occurences = {}
for i,j in zip(word_bank, X[0]):
    number_of_occurences[i] = [j, [1]*j]












# to find the position we will loop through the content until we find the word the number of times it occurs
print(number_of_occurences)
print('time taken:', time.time() - start_time)
