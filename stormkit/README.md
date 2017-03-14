# stormkit
A set of tools created by me to help with metadata anlaysis and generative art, including a implementation of sentiment analysis using the '[bag-of-words model](https://en.wikipedia.org/wiki/Bag-of-words_model)'. Designed to be lightweight with a very low computational time. Predominantly designed for small amounts of text. For example, tweets. It can currently detect, positivity, negativity, anger, worry, sadness and scare.

## How to install
Install via pip
```Shellscript
pip install stormkit
```

## The BasicSentimentAnalysis class
To initiate the class call
```python
sentiment = BasicSentimentAnalysis()
```
To analyse a string call the function analyse_text(), this will return a 'SentimentResult' object
```python
result = sen.analyse_text("I hate Trump, I'm furious, but I love ice cream.")
```
To check if any error occurred simply check the error variable, this should be done whenever creating a new 'SentimentResult' object
```python
if result.error is None:
    print result.percentages
else:
    print result.error
```
To get the results of the sentiment analysis use one of the following
```python
# this is the raw data, including everything from words matched, 
# occurrences and different types of mood. Good for debugging
result.raw

# this returns an array containing the string of the dominant 
# emotion(s) within the text, note - this can be more than one
result.majority_emotion

# this returns the decimals of emotions within the text 
# (in a dictionary), this is a float within the value of 0.0 
# and 1.0, the emotion name is the key
result.decimals

# this returns an array containing the words that were matched for
# the specified emotion, for example ["sad", "upset"]
result.words_for_emotion("angry")
```

## Word list files
The two word list files 'neg-lex.txt' and 'pos-lex.txt' are from http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html and are based on the following papers:

Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews." Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle, Washington, USA,
http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html

Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing 
and Comparing Opinions on the Web." Proceedings of the 14th 
International World Wide Web conference (WWW-2005), May 10-14, 
2005, Chiba, Japan.

The word list files 'angry-lex.txt', 'sad-lex.txt', 'worry-lex.txt' and 'scared-lex.txt' were created by me.
