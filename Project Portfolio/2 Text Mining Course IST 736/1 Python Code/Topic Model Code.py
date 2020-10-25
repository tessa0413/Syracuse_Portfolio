# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:15:02 2020

@author: Professor Gates - modified by jaci
"""
####################################################
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
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from mpl_toolkits.mplot3d import Axes3D
from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.feature_extraction.text import TfidfTransformer
import re
########################################################

##Code run on All Sources data set, and then ndivudal data sets for 
## each source.  Files names below: (change out last portion of URL)
## ABC_headline.csv, alj_headline.csv, bbc_headline.csv
## breitbart_headline.csv, cbs_headline.csv, cnn_headline.csv
## daily_headline.csv, fox_headline.csv, hill_headline.csv
## huffington_headline.csv, independent_headline.csv, metro_headline.csv
## mirror_headline.csv, # mirror_headline.csv, nbc_headline.csv
## NYT_headline.csv, reuters_headline.csv, verge_headline.csv

############################################################################# 



BIAS_DF=pd.read_csv('C:\\Users\\tessa\\OneDrive\\School\\Project Portfolio\\2 Text Mining Course IST 736\\0 Data Sets\\full_data.csv')
print(BIAS_DF.head())
# iterating the columns 
for col in BIAS_DF.columns: 
    print(col) 
    
print(BIAS_DF["Headline"])

### Tokenize and Vectorize the Headlines
## Create the list of headlines
HeadlineLIST=[]
for next in BIAS_DF["Headline"]:
    HeadlineLIST.append(next)

print("The headline list is")
print(HeadlineLIST)

### Vectorize
#https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
MyCountV=CountVectorizer(input="content", lowercase=True, stop_words = "english")
 
MyDTM = MyCountV.fit_transform(HeadlineLIST)  # create a sparse matrix
print(type(MyDTM))
#vocab is a vocabulary list
vocab = MyCountV.get_feature_names()  # change to a list

MyDTM = MyDTM.toarray()  # convert to a regular array
print(list(vocab)[10:20])
ColumnNames=MyCountV.get_feature_names()
MyDTM_DF=pd.DataFrame(MyDTM,columns=ColumnNames)
print(MyDTM_DF)


from sklearn.decomposition import NMF, LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer

num_topics = 5

lda_model_DH = LatentDirichletAllocation(n_components=num_topics, 
                                         max_iter=100, learning_method='online')
#lda_model = LatentDirichletAllocation(n_components=NUM_TOPICS, max_iter=10, learning_method='online')
LDA_DH_Model = lda_model_DH.fit_transform(MyDTM_DF)


print("SIZE: ", LDA_DH_Model.shape)  # (NO_DOCUMENTS, NO_TOPICS)

# Let's see how the first document in the corpus looks like in
## different topic spaces
print("First headline...")
print(LDA_DH_Model[0])
print("Sixth headline...")
print(LDA_DH_Model[5])

print(lda_model_DH.components_)


## implement a print function 
## REF: https://nlpforhackers.io/topic-modeling/
def print_topics(model, vectorizer, top_n=10):
    for idx, topic in enumerate(model.components_):
        print("Topic:  ", idx)
      
        print([(vectorizer.get_feature_names()[i], topic[i])
                        for i in topic.argsort()[:-top_n - 1:-1]])
                        ## gets top n elements in decreasing order
    

####### call the function above with our model and CountV
print_topics(lda_model_DH, MyCountV)


##########################################################################

##  Visualization Table ##

word_topic = np.array(lda_model_DH.components_)
word_topic = word_topic.transpose()

num_top_words = 10
vocab_array = np.asarray(vocab)

#fontsize_base = 70 / np.max(word_topic) # font size for word with largest share in corpus
fontsize_base = 10

for t in range(num_topics):
    plt.subplot(1, num_topics, t + 1)  # plot numbering starts with 1
    plt.ylim(0, num_top_words + 0.5)  # stretch the y-axis to accommodate the words
    plt.xticks([])  # remove x-axis markings ('ticks')
    plt.yticks([]) # remove y-axis markings ('ticks')
    plt.title('Topic #{}'.format(t))
    top_words_idx = np.argsort(word_topic[:,t])[::-1]  # descending order
    top_words_idx = top_words_idx[:num_top_words]
    top_words = vocab_array[top_words_idx]
    top_words_shares = word_topic[top_words_idx, t]
    for i, (word, share) in enumerate(zip(top_words, top_words_shares)):
        plt.text(0.3, num_top_words-i-0.5, word, fontsize=fontsize_base)
                 ##fontsize_base*share)

plt.tight_layout()
plt.show()
