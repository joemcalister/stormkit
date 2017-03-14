#!/usr/bin/python
import csv
import string
import decimal
import os
import sys
       
#### SENTIMENT CLASS ####        
class SentimentResult:
    raw = []
    majority_emotions = []
    decimals = {}
    error = None

    def __init__(self, results):
        self.raw = results

        # majority emotion
        current_highest = 0
        for dictionary in results:
            if int(dictionary["occurences"]) > current_highest:
                current_highest = int(dictionary["occurences"])
        if current_highest > 0:
            for dictionary in results:
                if int(dictionary["occurences"]) == current_highest:
                     self.majority_emotions.append(dictionary["emotion"])
        else:
            self.majority_emotions = ['neutral']

        # decimals
        total = 0
        for result in results:
            total+=result["occurences"]
        # get decimal values for the amount of emotions
        for result in results:
            if (total > 0):
                ## double float cast fixes interesting type bug
                ## round to two decimal places
                self.decimals[result["emotion"]] = round(decimal.Decimal(str(float(float(result["occurences"])/total))),2)
            else:
                self.decimals[result["emotion"]] = 0;


    def words_for_emotion(self,emotion):
        for emotions in self.raw:
            if emotions["emotion"] == emotion:
                return emotions["words"]
        return []



class MultiMoodSentimentAnalysis:
    """Multiple mood detection using sentiment analysis via the 'bag of words' model."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    word_dict_filenames = [['negative', dir_path+'/lists/neg-lex-strip.txt'],
                           ['positive', dir_path+'/lists/pos-lex-strip.txt'],
                           ['angry', dir_path+'/lists/angry-lex.txt'],
                           ['sad', dir_path+'/lists/sad-lex.txt'],
                           ['worried', dir_path+'/lists/worried-lex.txt'],
                           ['scared', dir_path+'/lists/scared-lex.txt']];
    word_dict = {}
    
    def __init__(self):
        #load in our word dictionaries
        for filedict in self.word_dict_filenames:
            with open(filedict[1], 'r') as f:
                temparray = f.readlines()
                #check for error reading words from lines
                if len(temparray) == 0:
                    raise Exception("No words found in dictionary, installation likely corrupt.");
                #strip whitespace too
                temparray = [x.strip() for x in temparray]
                self.word_dict[filedict[0]] = temparray
            #check that dictionaries are full, otherwise there's an issue
            if len(self.word_dict) == 0:
                raise Exception("Word dictionaries are empty, check installation of module.")

    def analyse_text(self,tweet):
        #individual words
        words = tweet.split(' ')
        #remove words
        words = self.remove_noise(words)
        #get skews
        skews = []
        for current_emotion in self.word_dict:
            returnedArray = self.get_skew(self.word_dict[current_emotion], words)
            skews.append({"occurences":len(returnedArray),
                          "emotion":current_emotion,
                          "words":returnedArray})
        #parse final results
        sen = SentimentResult(skews)
        return sen

        
    def get_skew(self, current_emotion, sentance):
        # return array of elements in both arrays
        return [x for x in current_emotion if x in sentance]
    

    def remove_noise(self,words):
        # loop through all words to remove sensitive ones
        for index, word in enumerate(words):
            #strip case
            word = word.lower()
            #remove any punctuation
            punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            no_punctuation = ""
            for char in word:
                if char not in punctuation:
                    no_punctuation = no_punctuation + char
            word = no_punctuation
            #set final value
            words[index] = word

        #return clean array 
        return words
