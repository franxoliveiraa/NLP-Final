# NLP-Final

Grace Wagner and Francisco Oliveira 

Overview: 
Movies have played an integral role in American popular culture since the development of the film industry in the early 20th century. With an estimated 96.1% of homes in the U.S. having a TV and the American film industry grossing billions of dollars each year, it is clear that film as a medium has been very culturally relevant and influential across the country.

As the visual effects seen in movies have naturally evolved with the development of new technology, we hypothesize that the content of movie dialogue has also changed over time in accordance with shifts in cultural sentiment, norms, and language usage. We aim to use language processing techniques on a large corpus of American movie subtitles from the 1930’s - 2010’s in order to determine if movie texts from a given decade share commonalities that are distinct from other time periods. Our project proposes that these trends may reveal interesting information about the differences between popular themes and informal communication across decades.

Data: 
The raw data we are using consist of the English subtitles for over 200,000 movies and television shows. This has been downloaded as a single text file from the Open Parallel Corpus (OPUS) website, who collected and compiled the data from OpenSubtitles.org. We were also able to download detailed metadata for each movie and TV episode in our dataset from English-Corpora.org, which maintains its own version of the OpenSubtitles collection. 

After removing (1) all of the TV episodes (2) all of the subtitles from movies that originated outside the U.S. and (3) any that do not have a year associated with them, our full dataset contained the subtitles to 13,430 movies.

We then randomly sampled 450 movies from each decade (4,050 movies total) for analysis through K-means clustering.

Lines from the movies in this sample were then grouped by an 80/20 train/test split (80% training data, 10% cluster test set, 10% random test set). For decade classification using distilBERT, we then randomly sampled lines from each set and trained the model on 500,000 lines and tested it on two test sets of 5,000 lines each.

OPUS (OpenSubtitles Collection): https://opus.nlpl.eu/OpenSubtitles-v2018.php
English Corpora: https://www.english-corpora.org/
OpenSubtitles.org: https://www.opensubtitles.org/en/search/subs

Method: 


Conclusions: 	




