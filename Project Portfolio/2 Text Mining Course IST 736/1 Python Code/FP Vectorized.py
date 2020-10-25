# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:18:40 2020

@author: junkm
"""


## Textmining Naive Bayes Example
import nltk
import pandas as pd
import sklearn
import re  
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
## For Stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import os

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import string

##################################

## Step 1: Read in the file
BiasDF="C:\\Users\\junkm\\OneDrive\\Documents\\DataFiles\\clean_data.csv"

## Read the new csv file you created into a DF or into CounterVectorizer
#######

MyTextDF=pd.read_csv(BiasDF)
## remove any rows with NA
MyTextDF = MyTextDF.dropna(how='any',axis=0)  ## axis 0 is rowwise
print(MyTextDF.head())
print(MyTextDF["Label"])
print(MyTextDF.iloc[1,1])

## KEEP THE LABELS!
MyLabel = MyTextDF["Label"]
## Remove the labels from the DF
DF_noLabel= MyTextDF.drop(["Label"], axis=1)  #axis 1 is column
#print(DF_noLabel.head())
## Create a list where each element in the list is a row from
## the file/DF
#print(DF_noLabel)
print("length: ", len(DF_noLabel))

### BUILD the LIST that "content" in CountVectorizer will expect
MyList=[]  #empty list
for i in range(0,len(DF_noLabel)):
    NextText=DF_noLabel.iloc[i,0]  ## what is this??
    ## PRINT TO FIND OUT!
    #print(MyTextDF.iloc[i,1])
    #print("Review #", i, "is: ", NextText, "\n\n")
    #print(type(NextText))
    ## This list is a collection of all the reviews. It will be HUGE
    MyList.append(NextText)

## see what this list looks like....
print(MyList[1:4])
    
########## Now we will vectorize!
## CountVectorizer takes input as content
## But- you cannot use "content" unless you know what
## this means and so what the CountVectorizer expects.
## "content" means that you will need a LIST that
## contains all the text. In other words, the first element in
## the LIST is ALL the text from review 1 (in this case)
## the second element in the LIST will be all the text from
## review 2, and so on...
## If you look ABOVE, the for loop BUILDS this LIST.
    ############################################################
MycountVect = CountVectorizer(input="content")

CV = MycountVect.fit_transform(MyList)

MyColumnNames=MycountVect.get_feature_names()
VectorizedDF_Text=pd.DataFrame(CV.toarray(),columns=MyColumnNames)
## Note - this DF starts at row 0 (not 1)
## My labels start at 1 so I need to shift by 1
print(VectorizedDF_Text)

### Put the labels back
## Make copy
print(MyLabel)
print(type(MyLabel))  

NEW_Labels = MyLabel.to_frame()   #index to 0
print(type(NEW_Labels))

NEW_Labels.index =NEW_Labels.index-1
print(NEW_Labels)

LabeledCLEAN_DF=VectorizedDF_Text
LabeledCLEAN_DF["LABEL"]=NEW_Labels
print(LabeledCLEAN_DF)