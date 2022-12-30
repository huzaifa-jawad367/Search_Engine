# Search_Engine
CS250 End of Semester project: Text based search engine

The end of semester search engine project consists of the following parts:
1. Preprocessing of data
2. Indexing
3. Searching

The pre-processing of data consisted of the following steps:
a. Cleaning the data
     i. Removing punctuation
    ii. Removing new line characters
   iii. Removing words containing numbers
    iv. Lowering text
![image](https://user-images.githubusercontent.com/103884662/210053963-e9ab72b9-782c-448c-84d5-8c7d3f700580.png)

b. Removing stopwords

![image](https://user-images.githubusercontent.com/103884662/210054015-0ac4f14b-ab1c-4ad5-a2b8-51a70a11f42a.png)
![image](https://user-images.githubusercontent.com/103884662/210054081-a0040106-e940-41f3-9e3b-1a6b1aca7624.png)

c. Lemmatizing the data (lemmatization resulted in better and cleaner words in the corpus compared to stemming)
![image](https://user-images.githubusercontent.com/103884662/210054118-0b45f21c-3758-45c8-842a-690c7bef6a20.png)

For indexing we created a forward index and then a lexicon using the forward index. The time it took to process 180000 files and removing files that had no content after which there was no content resulting in 160000 files. The result is the following:
![image](https://user-images.githubusercontent.com/103884662/210053893-cd191507-fb17-4435-8b73-d899c87736b4.png)

The project could not be completed in the given time frame only single word searching was implemented on the basis of position and frequency.
$DocScore = frequency * np.sum(1 - np.array([positions])/LengthOfArticle)$
