import os
import json

l = os.listdir('articles_dataset\json\\nela-gt-2021\\newsdata\\train')
length = 0
for i in l:
    fhand = open(f'articles_dataset\json\\nela-gt-2021\\newsdata\\train\{i}')
    x = json.loads(fhand.read())
    length += len(x)
    fhand.close()
    if length >= 150000:
        print(i)
        break

print(length)