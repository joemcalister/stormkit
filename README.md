#stormkit
This is a collection of tools created by me to help with my own artwork. It currently includes multiple-mood sentiment anlaysis (based on the bag of words model). Soon to include other tools including point of speech tagging.

##How to install
Easiest to install via pip:
```Shellscript
pip install stormkit
```

### Multiple Mood Sentiment Analaysis
This class can be used to determine the sentiment in text, for example the percentage of anger, sadness. It currently supports, positivity, negativity, anger, worry, sadness and scare.

Import the library
```python
from stormkit.sentimentAnalysis import *
```

To initiate the class call
```python
sentiment = BasicSentimentAnalysis()
```
To analyse a string call the function analyse_text(), this will return a 'SentimentResult' object
```python
result = sen.analyse_text("I hate Trump, I'm furious, but I love ice cream.")
```
To check if any errors occurred simply check the error variable, this should be done whenever creating a new 'SentimentResult' object
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