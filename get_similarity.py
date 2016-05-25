import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import difflib as dl
import HTMLParser
import re
import itertools

def stemming(data):
	data = data.split()
	p_stemmer = PorterStemmer()
	texts = [p_stemmer.stem(i) for i in data]
	return " ".join(texts)

def remove_stop(data):
	data = data.split()
	stop = stopwords.words('english')
	stopped_tokens = [i for i in data if i not in stop]
	return ' '.join(stopped_tokens)	

def tokenize(data):
	tokenizer = RegexpTokenizer(r'\w+')
	raw = data.lower()
	tokens = tokenizer.tokenize(raw)
	return tokens	

def remove_duplicate(data):
	data = sorted(data.split())
	data = set(data)
	return " ".join(data)

def DataClean(data):
	data = data.lower()
		
	#first step decoding data
	data = data.decode('utf-8').encode('ascii', 'ignore')
	
	#second step Parse HTML elements
	html_parser = HTMLParser.HTMLParser()
	data = html_parser.unescape(data)
	
	#remove stopwords
	data = remove_stop(data)
	
	#Standardizing words
	data = ''.join(''.join(s)[:2] for _, s in itertools.groupby(data))
	
	#stemming of data
	#data = stemming(data)
	
	#removal of duplicate words
	data = remove_duplicate(data)

	#remove of comma(,)
	data = re.sub(",", "", data)
	return data

def Grab_skills(data):
	#load skills keyword txt file
	f = open('keywords.txt').read()
	dat = f.split("\n")
	dat = set(dat)
	data = data.split()
	result = []
	for i in data:
		if i in dat:
			result.append(i)
	#return result
	return " ".join(result)	


def get_similarity():

	f1 = raw_input('Enter First Filename : ')
	f2 = raw_input('Enter second Filename : ')
	doc_a = open(f1).read()
	doc_b = open(f2).read()
		

	cleaned_b = DataClean(doc_b)
	cleaned_a = DataClean(doc_a)
	
	
	#grab skills
	skills_a = Grab_skills(cleaned_a)
 	skills_b = Grab_skills(cleaned_b)
	
	#print skills_a
	#print skills_b
	sim = dl.get_close_matches

	s = 0
	wa = skills_a.split()
	wb = skills_b.split()

	for i in wa:
	    if sim(i, wb):
		s += 1

	n = float(s) / float(len(wa))
	print round(n, 3)

if __name__ == '__main__':
	get_similarity()
