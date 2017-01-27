import data
import nltk
from nltk.tokenize import word_tokenize

class Brain:
	
	def __init__(self):
		self.train()
	
	def train(self):
		td = data.training_data
		self.all_words = set(word.lower() for passage in td for word in word_tokenize(passage[0]))
		t = [({word: (word in word_tokenize(x[0])) for word in self.all_words}, x[1]) for x in td]
		self.classifier = nltk.NaiveBayesClassifier.train(t)
		
	def getCommand(self, text):
		featurized_test_sentence = {i:(i in word_tokenize(text.lower())) for i in self.all_words}
		return self.classifier.classify(featurized_test_sentence)
	
	def getStats(self):
		print('stats', self.classifier.show_most_informative_features(10))