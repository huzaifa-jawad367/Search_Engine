from ForwardIndex import *
import json
import shutil
import time

def create_lexicon(forward_index):
    # initialize lexicon
    lexicon = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        lexicon[char] = {}
    lexicon['other'] = {}

    # for doc_id, word_data in forward_index.items():
    for doc_id in forward_index.keys():
        for word_id, data in zip(forward_index[doc_id].keys(), forward_index[doc_id].items()):
            # print(data)
            num_occurrences, hits = data
            if word_id[0] in 'abcdefghijklmnopqrstuvwxyz':
                try:
                    lexicon[word_id[0]][word_id][0] += 1
                except:
                    lexicon[word_id[0]][word_id] = [1]
                try:
                    lexicon[word_id[0]][word_id][1][doc_id] = hits
                except:
                    lexicon[word_id[0]][word_id].append({})
                    lexicon[word_id[0]][word_id][1][doc_id] = hits
            else:
                try:
                    lexicon['other'][word_id][0] += 1
                except:
                    lexicon['other'][word_id] = [1]
                try:
                    lexicon['other'][word_id][1][doc_id] = hits
                except:
                    lexicon['other'][word_id].append({})
                    lexicon['other'][word_id][1][doc_id] = hits

    return lexicon

forwardBarrel = forward_Indexing()

start_time = time.time()
lexi = create_lexicon(forwardBarrel)
print("Time taken for inverted indexing:", time.time()-start_time)

start_time = time.time()

if os.path.exists('Barrels'):
    shutil.rmtree('Barrels')
os.mkdir('Barrels')
for barrel in lexi.keys():
    with open(f'Barrels\Inverted_index{barrel}.json', 'w') as fhand:
        i_index = json.dumps(lexi[barrel], indent=2, cls=NpEncoder)
        fhand.write(i_index)
print("Time taken for writing to Lexicon:", time.time()-start_time)


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

