# text_preprocessing
Intro:
This project conduct a text preprocessing based on nltk twitter_samples. 


Methods:

0. create a text process object:
processor = tp.TextProcess()

1. calculating the average length of each piece in a corpus
average_length = processor.corpus_average_length(corpus)

2. strip hashtags(only lower English alphabat with 8 character longer will be stripped) from corpus such as instagram, twitter, etc.
hashtags = processor.hashtagProcessing(corpus)

3. hashtag hybrid tokenisation based on MaxMatch and a dictionary refered to nltk.corpus.words.words()
  eg. '#textpreprocessingproject'   -> 'text preoprocessing project'
tokenized_hashtags = processor.maxMatch_tokenizer(tokens)
 
4. implement interface for user to use their own stopwords
stopwords = processor.stop_word_dict(stopwords)

5. implement forward, backward maxmatch string tokenization
tokenized_string = processor.FMM(string,stopwords)
tokenized_string = processor.BMM(string,stopwords)
   
reference:
nltk




