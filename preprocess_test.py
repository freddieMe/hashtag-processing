from nltk.corpus import twitter_samples
import TextProcess as tp

"""
This code illustrate a way of testing with twitter_samples from nltk corpus.

make sure to download twitter_sample in first time execution
or have corpus with hashtags inside
"""

#nltk.download('twitter_samples')
corpus = twitter_samples.strings()

# create a Text Process object   
processor = tp.TextProcess()

# strip hashtags from corpus
tokens = processor.hashtagProcessing(corpus)
print(tokens)

#tokenize stripped hashtags
tokens = processor.maxMatch_tokenizer(tokens)
print(tokens)

