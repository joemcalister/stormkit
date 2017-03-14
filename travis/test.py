from stormkit.sentimentAnalysis import *

sen = MultiMoodSentimentAnalysis()
result = sen.analyse_text("I hate Trump, I'm furious, but I love ice cream. Such a saddening moment. I'm frightened to be honest")

if result.error is None:
    print(result.raw)
    assert True
else:
    assert False
