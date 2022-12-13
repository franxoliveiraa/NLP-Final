import gensim
import numpy as np
import pandas as pd
import random
from gensim.models import Word2Vec
from sklearn.cluster import KMeans

## This file finds the subtitles closest to the center of each cluster

# Load word2vec model
model = Word2Vec.load("word2vec.model")


# Get metadata of movies in sample
sample_movie_indices = []
sample_metadata = []

sample_file = pd.read_excel("sample_movie_metadata.xlsx", sheet_name='Sample')
sample_df = pd.DataFrame(sample_file, columns=['index','textID','title','year','decade','genre'])
sample_movie_indices = sample_df['index'].tolist()
sample_movie_indices = [int(i) for i in sample_movie_indices]
ids = sample_df['textID'].tolist()
titles = sample_df['title'].tolist()
decades = sample_df['decade'].tolist()
years = sample_df['year'].tolist()
genres = sample_df['genre'].tolist()
for i in range(len(sample_movie_indices)):
    index = sample_movie_indices[i]
    id = ids[i]
    title = titles[i]
    decade = decades[i]
    year = years[i]
    genre = genres[i]
    meta = [index, id, title, year, decade, genre]
    sample_metadata.append(meta)
print("READ METADATA\n")


# Load movie vectors from file
movievectors = []
with open('movie_vectors', 'r') as fread:
    file = fread.read().rstrip()
    vectors = file.replace("[", "").strip().split(']')
    for i in range(4050):
        current = np.zeros(100)
        values = vectors[i].split()
        for j in range(100):
            current[j] = current[j] + float(values[j].strip('\n'))
        movievectors.append(current)
print("READ " + str(len(movievectors)) + " MOVIE VECTORS\n")

# Cluster movies
num_clusters = 30
kmmovies = KMeans(n_clusters=num_clusters, random_state=0)
movieclusters = kmmovies.fit_predict(movievectors)
centers = kmmovies.cluster_centers_

# Read all subtitles in sample
with open('sample_subtitles_data', 'r') as f:
    all_lines = f.readlines()
print("READ ALL LINES\n")

# Get ~500,000 lines for cluster test set
with open('test_cluster', 'w') as out, open('test_cluster_lines', 'w') as line_file:
    for i in range(num_clusters):
        lineclusterdistances = []
        # Get list of movies in the cluster
        movies = []
        for j in range(len(movieclusters)):
            if movieclusters[j] == i:
                movies.append(j)
        # Get closest lines for each cluster
        line_num = 0
        for line in all_lines:
            sub = line.split(',')
            if int(sub[2]) in movies:
                totvec = np.zeros(100)
                for token in sub[0].split(" "):
                    try:
                        totvec = totvec + model.wv[token]
                    except KeyError:
                        continue
                dist = np.linalg.norm(totvec-(centers[i]))
                if len(lineclusterdistances) < 16900:
                    lineclusterdistances.append((dist,sub[0],sub[1],line_num))
                elif dist < lineclusterdistances[-1][0]:
                    lineclusterdistances[-1] = (dist,sub[0],sub[1],line_num)
                lineclusterdistances.sort(key = lambda x: x[0])
            line_num += 1
            if line_num%1000000==0:
                print("Running...")
        lines = [(item[1],item[2],item[3]) for item in lineclusterdistances]
        for line in lines:
            out.write(line[0]+','+line[1]+'\n')
            line_file.write(str(line[2])+',')   ## Write cluster line numbers to file (to be excluded from train/test data)
        print("CLUSTER " + str(i))


# Write all subtitles and cluster test subtitles to csv
def read_csv():
    read_cluster = pd.read_csv('test_cluster',header=None)
    read_cluster.columns=['text','label']
    read_cluster.to_csv ('test_cluster.csv', index=None)

    read_all = pd.read_csv('sample_subtitles_data',header=None)
    read_all.columns=['text','label','index']
    read_all.to_csv ('sample_subtitles_data.csv', index=None)
