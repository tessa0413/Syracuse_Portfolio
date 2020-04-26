# -*- coding: utf-8 -*-
"""
Created on Fri Feb 7 2020

@author: Prof Gates modified by Jaci W
"""

import nltk
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
## For Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import os

biasdata = pd.read_csv("C:\\Users\\tessa\\OneDrive\\School\\Project Portfolio\\2 Text Mining Course IST 736\\0 Data Sets\\clean_data.csv")
biasdata.head()

class LemmaTokenizer(object):
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, articles):
        return [self.wnl.lemmatize(t) for t in word_tokenize(articles) if t not in stopwords.words('english') or string.punctuation]
    
class LemmaTokenizer(object):
    def __call__(self, text):
        return [lemma(t) for t in word_tokenize(text) if t not in stopwords.words('english')]

## Build the vectorizer
pattern='r/^[a-zA-Z]{4}$/'
pattern="[^r\P{P}]+"

MyVect5=CountVectorizer(biasdata,
                        analyzer = 'word',
                        stop_words='english',
                           #token_pattern='(?u)[a-zA-Z]+',
                        #token_pattern=pattern,
                        #tokenizer=LemmaTokenizer(),
                        #strip_accents = 'unicode', 
                        lowercase = True
                        )

MyVect5B=CountVectorizer(biasdata,
                        analyzer = 'word',
                        stop_words='english',
                          #token_pattern='(?u)[a-zA-Z]+',
                        #token_pattern=pattern,
                        #tokenizer=LemmaTokenizer(),
                        #strip_accents = 'unicode', 
                        binary=True
                        )
FinalDF=pd.DataFrame()
FinalDFB=pd.DataFrame()
MyVect5
MyVect5B


#####################################################################################################
## Replace the NaN with 0 because it actually 
## means none in this case
FinalDF=biasdata.fillna(0)
X5=MyVect5.fit_transform(FinalDF)
ColumnNames2=MyVect5.get_feature_names()
print("Column names: ", ColumnNames2)
FinalDFB=biasdata.fillna(0)
X5B=MyVect5B.fit_transform(FinalDFB)
print("FIRST...Normal DF Freq")  ## These print statements help you to see where you are
print(FinalDF)
print("BINARY DF....")
print(FinalDFB)


##############################################################################################################

      

## Create the testing set - grab a sample from the training set. 
## Be careful. Notice that right now, our train set is sorted by label.
## If your train set is large enough, you can take a random sample.
from sklearn.model_selection import train_test_split

TrainDF, TestDF = train_test_split(FinalDF, test_size=0.3)



##-----------------------------------------------------------------
##
## Now we have a training set and a testing set. 
print("The training set is:")
print(TrainDF)
print("The testing set is:")
print(TestDF)

## IMPORTANT - YOU CANNOT LEAVE LABELS ON THE TEST SET
## Save labels
TestLabels=TestDF["Label"]
print(TestLabels)
## remove labels
TestDF = TestDF.drop(["Label"], axis=1)
print(TestDF)





####################################################################
########################### Naive Bayes ############################
####################################################################
from sklearn.naive_bayes import MultinomialNB
#https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html#sklearn.naive_bayes.MultinomialNB.fit
#Create the modeler
MyModelNB= MultinomialNB()
## When you look up this model, you learn that it wants the 
## DF seperate from the labels
TrainDF_nolabels=TrainDF.drop(["Label"], axis=1)
print(TrainDF_nolabels)
TrainLabels=TrainDF["Label"]
print(TrainLabels)

MyModelNB.fit(TrainDF_nolabels, TrainLabels)

Prediction = MyModelNB.predict(TestDF)
print("The prediction from NB is:")
print(Prediction)
print("The actual labels are:")
print(TestLabels)
## confusion matrix
from sklearn.metrics import confusion_matrix
## The confusion matrix is square and is labels X labels
## We ahve two labels, so ours will be 2X2
#The matrix shows
## rows are the true labels
## columns are predicted
## it is al[habetical
## The numbers are how many 
cnf_matrix = confusion_matrix(TestLabels, Prediction)
print("The confusion matrix is:")
print(cnf_matrix)
### prediction probabilities
## columns are the labels in alphabetical order
## The decinal in the matrix are the prob of being
## that label
print(np.round(MyModelNB.predict_proba(TestDF),2))

#######################################################
### Bernoulli #########################################
#######################################################
### NOTE TO CLASS: This should use the Binary
## DF and is not correct - be sure to fix it :)


print(FinalDFB)
print(TestDF)

FinalDFB_nolabels=FinalDFB.drop(["Label"], axis=1)
print(FinalDFB_nolabels)
FinalLabels=FinalDFB["Label"]
print(FinalLabels)

from sklearn.naive_bayes import BernoulliNB
BernModel = BernoulliNB()
BernModel.fit(TrainDF_nolabels, TrainLabels)
BernoulliNB(alpha=3.0, binarize=0.0, class_prior=None, fit_prior=True)
print("Bernoulli prediction:", BernModel.predict(FinalDFB_nolabels))
print("Actual:")
print(FinalLabels)

#############################################
###########  SVM ############################
#############################################
from sklearn.svm import LinearSVC
SVM_Model=LinearSVC(C=10)
SVM_Model.fit(TrainDF_nolabels, TrainLabels)
BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
print("SVM prediction:\n", SVM_Model.predict(FinalDFB_nolabels))
print("Actual:")
print(FinalLabels)

###########################################################################



