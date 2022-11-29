# NLP-Final

Grace Wagner and Francisco Oliveira 

Overview: 
Movies have played an integral role in American popular culture since the development of the film industry in the early 20th century. With an estimated 96.1% of homes in the U.S. having a TV and the American film industry grossing billions of dollars each year, it is clear that film as a medium has been very culturally relevant and influential across the country.

As the visual effects seen in movies have naturally evolved with the development of new technology, we hypothesize that the content of movie dialogue has also changed over time in accordance with shifts in cultural sentiment, norms, and language usage. We aim to use language processing techniques on a large corpus of American movie subtitles from the 1930’s - 2010’s in order to determine if movie texts from a given decade share commonalities that are distinct from other time periods. Our project proposes that these trends may reveal interesting information about the cultural conditions and/or styles of informal communication in each decade.

Data: 
The raw data we are using consist of the English subtitles for over 200,000 movies and television shows. This has been downloaded as a single text file from the Open Parallel Corpus (OPUS) website, who collected and compiled the data from OpenSubtitles.org. We were also able to download detailed metadata for each movie and TV episode in our dataset from English-Corpora.org, which maintains its own version of the OpenSubtitles collection. Our next step in compiling the data is to map the plaintext subtitles for each movie/TV episode to its corresponding metadata. Then, we will remove from the dataset (1) all of the TV episodes (2) all of the subtitles from movies that originated outside the U.S. and (3) any that do not have a year associated with them. 

OPUS (OpenSubtitles Collection): https://opus.nlpl.eu/OpenSubtitles-v2018.php
English Corpora: https://www.english-corpora.org/
OpenSubtitles.org: https://www.opensubtitles.org/en/search/subs

Method: 
First, we plan to utilize simple topic modeling techniques on the entire dataset in order to cluster all of the movies based on text similarity. This will be done by obtaining vector representations of each movie text using the word2vec neural network model, then we will apply K-means clustering to the resulting vectors and graph all of the clusters with each individual movie colored according to its decade. This visualization will reveal if movies from the same decade are more similar to each other with respect to textual content and, consequently, have been clustered together with some degree of frequency. 

Second, we will train a BERT model on subtitle texts labeled with the appropriate decade of origin and analyze the model’s performance when classifying test text that is closely associated with a given cluster versus randomly selected from the corpus. This first will involve randomly splitting the dataset into train (80%) and test (20%) sets with proportional representations of movies from each decade. Then, we will delineate two sets of test data: one containing subtitles that have word embedding vectors very close to the central point of each cluster and another containing randomly selected subtitles. The trained BERT model will then be used to classify both test sets by decade and the performance between the two will be compared (see Evaluation).

Evaluation: 	
For the primary quantitative analysis, the performance of the BERT model in classifying the two test sets will be directly compared. A difference in model performance when using text that closely captures a cluster’s topic will reveal if the cluster, which is determined based on content similarity across all movies, is in any way indicative of the movie’s decade of origin. We will also analyze each of the clusters to determine what the overarching topics of each seem to be, and we will attempt to draw cultural conclusions about each time period from the clusters if they seem to be correlated with movies from certain decades.

In regards to qualitative analysis, we aim to graphically represent our clustering over social and historical phenomena, providing both a general overview of film sentiment through the past century, and a narrowed view of film sentiment per decade. 



References

Lison, Pierre and Jörg Tiedemann. (2016). “OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles.” In Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016).

Suzanna Sia, Ayush Dalmia, and Sabrina Mielke. (2020). “Tired of Topic Models? Clusters of Pretrained Word Embeddings Make for Fast and Good Topics too!” In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 1729-1736. 

Radu Tudor Ionescu and Andrei Butnaru. (2019). “Vector of Locally-Aggregated Word Embeddings (VLAWE): A Novel Document-level Representation.” In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pp. 363–369.

Pierre Lison,  Jorg Tiedemann, and Milen Kouylekov. (2018). “OpenSubtitles2018: Statistical Rescoring of Sentence Alignments in Large, Noisy Parallel Corpora.” 

​​Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 4171–4186, Minneapolis, Minnesota. Association for Computational Linguistics.



