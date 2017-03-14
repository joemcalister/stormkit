from stormkit.sentimentAnalysis import *

# create sentiment class
sen = MultiMoodSentimentAnalysis()

# pass in the text and collect the result object
result = sen.analyse_text("I hate Trump, I'm furious, but I love ice cream. Such a saddening, frightning, moment.")

# print out the results and potentially collect any errors
if result.error is None:
    assert true
else:
    assert false
