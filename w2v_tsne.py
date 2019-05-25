print("Importing libraries...")

import gensim.models.word2vec as w2v
import os
import sys
from sklearn.manifold import TSNE
from pandas import DataFrame

print("Loading trained model...")
try:
	book2vec = w2v.Word2Vec.load(sys.argv[1])
except:
	print("Failed to load model. Please check if you provided a correct file path.")
	exit()

print("Performing dimensionality reduction... Please wait...")

tsne = TSNE(n_components=2, random_state=0, metric = 'cosine')
all_word_vectors_matrix = book2vec.wv.vectors
all_word_vectors_matrix_2d = tsne.fit_transform(all_word_vectors_matrix)

print("Saving the files...")

points = DataFrame(
    [
        (word, coords[0], coords[1], attr)
        for word, coords, attr in [
            (word, all_word_vectors_matrix_2d[book2vec.wv.vocab[word].index], "attr")
            for word in book2vec.wv.vocab
        ]
    ],
    columns=["word", "x", "y", "attr"]
)

if not os.path.exists("data"):
    os.makedirs("data")
book2vec.save(os.path.join("data", "book2vec.w2v"))
points.to_pickle("data/reduced_book.pkl")

print("Done!")