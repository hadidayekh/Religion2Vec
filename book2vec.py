import codecs
import glob
import multiprocessing
import os
from gensim.models.word2vec import Word2Vec as w2v
from pandas import read_pickle
from pandas import Series as pd_Series
import sys
from json import dumps as json_dumps

book = sys.argv[1]
book2vec = w2v.load(os.path.join(book+ "2Vec_trained", "trained", book + "2vec.w2v"))
points = read_pickle(book + "2Vec_trained/reduced_" + book + ".pkl")


def get_word_count(word, word_vectors):
	try:
		retVal = word_vectors.vocab[word].count
	except:
		retVal = 0
	return retVal
	
def get_most_similar_coordinates(word, count=10, pos='any', remove_stop=True): ##
	word = word.lower()
	word_vectors = book2vec.wv
	
	try:
		word_seq = word_vectors.most_similar(word, topn=len(word_vectors.vocab))
		sim_words = [x[0] for x in word_seq]
		if(remove_stop):
			#from nltk.corpus import stopwords
			#nltk.download("stopwords")
			#stop_words = set(stopwords.words('english'))
			stop_words = {'a','about','above','after','again','against','ain','all','am','an','and','any','are','aren',
			"aren't",'as','at','be','because','been','before','being','below','between','both','but','by','can','couldn',"couldn't",'d','did','didn',"didn't",'do','does','doesn',
			"doesn't",'doing','don',"don't",'down','during','each','few','for','from','further','had','hadn',"hadn't",'has','hasn',"hasn't",'have','haven',"haven't",
			'having','he','her','here','hers','herself','him','himself','his','how','i','if','in','into','is','isn',"isn't",'it',"it's",'its','itself','just',
			'll','m','ma','me','mightn',"mightn't",'more','most','mustn',"mustn't",'my','myself','needn',"needn't",'no','nor','not',
			'now','o','of','off','on','once','only','or','other','our','ours','ourselves','out',
			'over','own','re','s','same','shan',"shan't",'she',"she's",'should',"should've",'shouldn',"shouldn't",
			'so','some','such','t','than','that',"that'll",'the','their','theirs','them','themselves','then','there','these','they','this','those','through',
			'to','too','under','until','up','ve','very','was','wasn',"wasn't",'we','were','weren',"weren't",'what','when','where','which','while',
			'who','whom','why','will','with','won',"won't",'wouldn',"wouldn't",'y','you',
			"you'd","you'll","you're","you've",'your','yours','yourself','yourselves'}
			without_stop = [x for x in sim_words if x not in stop_words]
			sim_words = without_stop
		
		slice2 = points
		if pos != 'any':
			slice2 = points.loc[points['attr'].isin([pos])]
		attr_words = slice2['word'].tolist()
		res_words = [x for x in sim_words if x in attr_words]
		res_words = res_words[:count]

		slice = points.loc[points['word'].isin(res_words)]

		slice = slice.append(points.loc[points['word'] == word])
		slice['sim_score'] = pd_Series(1.0, index = slice.index)
		slice['word_count'] = pd_Series(0, index = slice.index)
		for i, point in slice.iterrows():
			slice.at[i, 'word_count'] = get_word_count(point.word, word_vectors)
			for (w, s) in word_seq:
				if w == point.word:
					slice.at[i, 'sim_score'] = round(s,3)
					break
		
		
		retVal = slice
	except:
		retVal = None
	return retVal


##print("hello")

d = get_most_similar_coordinates(sys.argv[2], int(sys.argv[3]), sys.argv[4])
if d is None:
	print ('absent')
else:
	df = d.to_dict(orient='records')
	temp = json_dumps(df)
	print(temp)


