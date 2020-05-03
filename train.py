import sys
import re

en = open('Tatoeba.en-es.en', 'r')
es = open('Tatoeba.en-es.es', 'r')

bigrams = {}

flag = True
while flag:
	line1 = re.sub(r'[^\w\s]','',en.readline().strip().lower())
	line2 = re.sub(r'[^\w\s]','',es.readline().strip().lower())
	if line1 == '' or line2 == '':
		flag = False
	for word1 in line1.split():
		for word2 in line2.split():
			if word1 not in bigrams:
				bigrams[word1] = {}
			if word2 not in bigrams[word1]:
				bigrams[word1][word2] = 1
			else:
				bigrams[word1][word2] +=1

#create my probabilistic dictionary and fill with stuff
myProb = open("en-es.tsv", "w+")
for key in bigrams:
	occurances = sum(bigrams[key].values())
	likeliest = ""
	bestProb = 0
	for word in bigrams[key]:
		if bigrams[key][word]/occurances > bestProb:
			bestProb = bigrams[key][word]/occurances
			likeliest = word
	myProb.write(str(bestProb) + " " + key + " " + likeliest + "\n")

myProb.close()
