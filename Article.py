#from nltk import 

class Article:
    #article no nlp features
    abstract = ""
    title = ""

    #nlp features
    tokens = []
    tf = []
    tfidf = []

    def __init__(self, abstract, title):
        self.abstract = abstract
        self.title = title
        # normalizing, tokenizing, stemming, lemmatizing, and making tf vector

