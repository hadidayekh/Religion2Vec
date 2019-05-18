from __future__ import absolute_import, division, print_function
import multiprocessing
import os
import gensim.models.word2vec as w2v
from gensim import utils, matutils
import sys
book = sys.argv[1]
book2vec = w2v.Word2Vec.load(os.path.join(book + "2Vec_trained", "trained", book + "2vec.w2v"))

def nearest_sim_diff(start1, end1, end2, num=1):
    start1 = start1.lower()
    end1 = end1.lower()
    end2 = end2.lower()
    try:
        similarities = book2vec.wv.most_similar_cosmul(
            positive=[end2, start1],
            negative=[end1],
            topn = num
        )
        start2 = similarities[0][0]
        #print("{start1} is related to {end1}, as {start2} is related to {end2}".format(**locals()))
        sims = [x[0] for x in similarities]
        return sims
    except:
        return None

retVal = nearest_sim_diff(sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5]))

if retVal is None:
    print( 'absent')
else:
    print(retVal)