from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			#increase
			worddictionary[word] += 1
		else:
			#add to the dictionary
			worddictionary[word]  = 1
    
    # sortedWords = sorted(worddictionary.items(), key = operator.itemgetter(1), reverse = 2)

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'worddictionary':worddictionary.items})