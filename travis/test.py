from stormkit.sentimentAnalysis import *

sen = MultiMoodSentimentAnalysis()
result = sen.analyse_text("I hate Trump, I'm furious, but I love ice cream. Such a saddening, frightning, moment.")

if result.error is None:
    print result.decimals
    assert True
else:
    assert False
