from ForwardIndex import *
from collections import defaultdict
import json
import time

def create_lexicon(forward_index):
    # initialize lexicon
    lexicon = {}

    # for doc_id, word_data in forward_index.items():
    for doc_id in forward_index.keys():
        for word_id, data in zip(forward_index[doc_id].keys(), forward_index[doc_id].items()):
            # print(data)
            num_occurrences, hits = data
            try:
                lexicon[word_id][0] += 1
            except:
                lexicon[word_id] = [1]
            try:
                lexicon[word_id][1][doc_id] = hits
            except:
                lexicon[word_id].append({})
                lexicon[word_id][1][doc_id] = hits

    return lexicon

forwardBarrel = forward_Indexing()

start_time = time.time()
lexi = create_lexicon(forwardBarrel)
print("Time taken for inverted indexing:", time.time()-start_time)

i_index = json.dumps(create_lexicon(forwardBarrel), cls=NpEncoder, indent=2)

with open('Inverted_index.json', 'w') as fhand:
    fhand.write(i_index)



# import json

# forward_Barrel =  json.loads("datasets\json\nela-gt-2021\newsdata\train\21stcenturywire.json")

# """forwardIndex = {docID:{wordIDs : nhits, ([hits])}}
# backwardIndex = {wordID:}"""
# forward_Index = {1:{"harvard":[8,[[12,'l'],[30,'u']]]}}
# # get a set of word ids 
# set_of_words = set({})
# for i in forward_Barrel:
#     for j in i.keys():
#         set_of_words = set_of_words.union(set(i[j]))

# word_occurences = {}
# for i in set_of_words:
#     word_occurences[i] = 0

# Inverted_Index = {"harvard":[0,[[],[],[]]]}
# for i in forward_Index.keys:
#     for j in forward_Index[i].keys:
#         if j in Inverted_Index.keys:
#             Inverted_Index[j][0] += 1
#             Inverted_Index[j][1].append((i,forward_Index[i][j][0],forward_Index[i][j][1]))
#         else:
#             Inverted_Index[j][0] = 1
#             Inverted_Index[j][1].append((i,forward_Index[i][j][0],forward_Index[i][j][1]))

