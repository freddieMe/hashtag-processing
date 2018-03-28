import nltk
import json
import re
from nltk.stem import WordNetLemmatizer  
from nltk.corpus import words 

class TextProcess(object):
           
    def __init__(self):
        print("text processor constructed")
        
    def corpus_average_length(self,corpus):
        """return average length of each piece of sample corpus
        para: corpus: list<twitter_samples.strings>
        return: average length of each piece in a corpus
        """    
        corpus_length = 0
        num_of_tweets = 0

        for ele, string in enumerate(corpus):
            corpus_length = len(string) + tweets_length
            num_of_tweets = ele
        average = corpus_length / num_of_tweets
        return average

    def hashtagProcessing(self,corpus):
        """strip hashtags from corpus
           all stripprd hashtags will be all lower letter alphabet,
           at least length of 8 long
        para: corpus: list<twitter_samples.strings>
        return: a list of stripped hashtags
        """
        hashtags = []
    
        for doc in corpus:     
            tags = []
            doc = doc.replace(" ","  ")
            tags += re.findall(r'^#[a-z]{8,}\s',doc) + \
                re.findall(r'\s#[a-z]{8,}$',doc) + \
                re.findall(r'\s#[a-z]{8,}\s',doc)
            for tag in tags:
                stripped_hash = re.sub(r'\s?#([a-z]{8,})\s?',r'\1',tag)
                hashtags.append(stripped_hash)
        return hashtags



    def stop_word_dict(self,stopwords):
        """construct a look-up dictionary for stopwords
        and decrease the search complexity to O(1)
        para: stopwords: a list of stopwords
        return: d(stopwords): dictionary format stopwords  
        """
        d = {}
        for word in stopwords:
            d[word] = d.get(word,0) + 1
        return d

    def BMM(self, string, stopwords):
        """Backward MaxMatch string tokenization
        para: string: a string that need to be tokenized
        para: stopword: dictionary format stopwords set
        return: tokenized string
        """    
        #create a lemmatizer object
        wordnet_lemmatizer = WordNetLemmatizer()        
        pos2 = len(string)  
        result = ''  
        while len(string) > 0:         
            word = wordnet_lemmatizer.lemmatize(string[0:pos2])  
            if stopwords.get(word):  
                result = result + string[0:pos2] + ' '  
                string = string[pos2:]  
                pos2 = len(string)  
            else:  
                pos2 = pos2-1
        return result
    
    
   
    def FMM(self, string, dic):
        """forward maxmatch string tokenization
        para: string: a string that need to be tokenized
        para: stopword: dictionary format stopwords set
        return: tokenized string
        """
        #create a lemmatizer object
        wordnet_lemmatizer = WordNetLemmatizer()
        tokenized = []
        start = 0  
        result = ''  
        while len(string) > 0:         
            word = wordnet_lemmatizer.lemmatize(string[start:])  
            if dic.get(word):
                result = string[start:] + ' ' + result
                string = string[0:start]
                start = 0
            else:  
                start = start + 1

        return result
    
    
    
    def maxMatch_tokenizer(self,tokens):
        """forward and backword maxmatch tokenization approach
        para: tokens: a list of tokens that waiting to be tokenized
        return: a list of tokenized tokens
        
        """
        tokenized = []
        wordlist = words.words()
        dic = self.stop_word_dict(wordlist) 
        for tag in tokens:
            h1 = self.BMM(tag, dic)
            h2 = self.FMM(tag, dic)
            if len(h1) < len(h2):
                tokenized.append(h1)
            else:
                tokenized.append(h2)
        return tokenized
            
    
    
    


    

