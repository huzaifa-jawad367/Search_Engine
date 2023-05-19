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

The inverted index json file was too big to uppload on either LMS or github

## Future Work to be done
* Improve search relevancy: Experiment with different ranking algorithms or techniques to enhance the relevancy of search results. Consider incorporating machine learning algorithms or natural language processing techniques to better understand user queries and improve the ranking of search results accordingly.

* Expand data sources: Currently, your search engine may be based on a limited set of articles. Consider expanding the scope by crawling and indexing more diverse sources of information, such as websites, blogs, forums, or social media platforms. This will provide users with a wider range of search results.

* User interface enhancements: Enhance the user interface to provide a more intuitive and user-friendly search experience. Consider implementing features like autocomplete suggestions, search filters, or advanced search options to help users refine their queries and find relevant information more efficiently.

* Incorporate query logs and user feedback: Analyze user search logs and feedback to gain insights into user behavior and preferences. Use this information to improve search results, personalize recommendations, or identify popular topics that can be highlighted in the search interface.

* Implement advanced features: Consider adding features such as spelling correction, synonym expansion, query expansion, or semantic search to make the search engine more robust and capable of handling variations in user queries. These features can help improve the accuracy and relevance of search results.

* Explore scalability and performance: Optimize your search engine for scalability and performance. As the volume of indexed documents and user queries increases, ensure that your system can handle the load efficiently. Explore techniques such as distributed indexing, caching, or parallel processing to improve the overall performance of the search engine.

* Integration with external tools: Explore integrating your search engine with other tools or platforms. For example, you could integrate with a recommendation system to provide personalized search results or integrate with a content management system to enable indexing and searching within specific domains or repositories.

* Mobile and voice search: Adapt your search engine to support mobile devices and voice-based interactions. Develop a mobile-friendly interface or create a voice-enabled search capability to cater to users who prefer using their smartphones or voice assistants for search.
