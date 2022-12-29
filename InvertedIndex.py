import json

forward_Barrel =  json.loads("datasets\json\nela-gt-2021\newsdata\train\21stcenturywire.json")

"""forwardIndex = {docID:{wordIDs : nhits, ([hits])}}
backwardIndex = {wordID:}"""
forward_Index = {1:{"harvard":[8,[[12,'l'],[30,'u']]]}}
# get a set of word ids 
set_of_words = set({})
for i in forward_Barrel:
    for j in i.keys():
        set_of_words = set_of_words.union(set(i[j]))

word_occurences = {}
for i in set_of_words:
    word_occurences[i] = 0

Inverted_Index = {"harvard":[0,[[],[],[]]]}
for i in forward_Index.keys:
    for j in forward_Index[i].keys:
        if j in Inverted_Index.keys:
            Inverted_Index[j][0] += 1
            Inverted_Index[j][1].append((i,forward_Index[i][j][0],forward_Index[i][j][1]))
        else:
            Inverted_Index[j][0] = 1
            Inverted_Index[j][1].append((i,forward_Index[i][j][0],forward_Index[i][j][1]))

