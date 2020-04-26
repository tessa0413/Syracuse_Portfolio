# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 11:20:15 2020

@author: tessa and jaci

Team Project IST736
"""

#%% Load Libraries
import nltk
nltk.download('punkt')
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
nltk.download('stopwords')
from nltk.corpus import stopwords
from wordcloud import WordCloud
import mediacloud.api, json, datetime
from dotenv import load_dotenv
import os
#%%
data = pd.read_csv('C:\\Users\\tessa\\OneDrive\\School\\Project Portfolio\\2 Text Mining Course IST 736\\0 Data Sets\\full_data.csv')
print(data)
#%%
grouped = data.groupby('source').groups

for group in grouped:
    NewsOutlet = print(group)

print(NewsOutlet)

for line in grouped: 
    print(line +" = data[data['source']=='" + line +"']")
#%% Separate Datasets for visual
ABCNews = data[data['source']=='ABC News']
AlJazeeraEnglish = data[data['source']=='Al Jazeera English']
BBCNews = data[data['source']=='BBC News']
BreitbartNews = data[data['source']=='Breitbart News']
CBSNews = data[data['source']=='CBS News']
CNN = data[data['source']=='CNN']
DailyMail = data[data['source']=='Daily Mail']
FoxNews = data[data['source']=='Fox News']
Independent = data[data['source']=='Independent']
Metro = data[data['source']=='Metro']
Mirror = data[data['source']=='Mirror']
NBCNews = data[data['source']=='NBC News']
Reuters = data[data['source']=='Reuters']
TheHill = data[data['source']=='The Hill']
TheHuffingtonPost = data[data['source']=='The Huffington Post']
TheNewYorkTimes = data[data['source']=='The New York Times']
TheVerge = data[data['source']=='The Verge']
#%%
for line in grouped:
    print(line + "Str = str(" +line + "['description'])")

#%%
ABCNewsStr = str(ABCNews['description'])
AlJazeeraEnglishStr = str(AlJazeeraEnglish['description'])
BBCNewsStr = str(BBCNews['description'])
BreitbartNewsStr = str(BreitbartNews['description'])
CBSNewsStr = str(CBSNews['description'])
CNNStr = str(CNN['description'])
DailyMailStr = str(DailyMail['description'])
FoxNewsStr = str(FoxNews['description'])
IndependentStr = str(Independent['description'])
MetroStr = str(Metro['description'])
MirrorStr = str(Mirror['description'])
NBCNewsStr = str(NBCNews['description'])
ReutersStr = str(Reuters['description'])
TheHillStr = str(TheHill['description'])
TheHuffingtonPostStr = str(TheHuffingtonPost['description'])
TheNewYorkTimesStr = str(TheNewYorkTimes['description'])
TheVergeStr = str(TheVerge['description'])

dataStr = str(data['description'])
#%%
for line in grouped:
    print(line + "Tok = word_tokenize(" + line + "Str)")

#%%
ABCNewsTok = word_tokenize(ABCNewsStr)
AlJazeeraEnglishTok = word_tokenize(AlJazeeraEnglishStr)
BBCNewsTok = word_tokenize(BBCNewsStr)
BreitbartNewsTok = word_tokenize(BreitbartNewsStr)
CBSNewsTok = word_tokenize(CBSNewsStr)
CNNTok = word_tokenize(CNNStr)
DailyMailTok = word_tokenize(DailyMailStr)
FoxNewsTok = word_tokenize(FoxNewsStr)
IndependentTok = word_tokenize(IndependentStr)
MetroTok = word_tokenize(MetroStr)
MirrorTok = word_tokenize(MirrorStr)
NBCNewsTok = word_tokenize(NBCNewsStr)
ReutersTok = word_tokenize(ReutersStr)
TheHillTok = word_tokenize(TheHillStr)
TheHuffingtonPostTok = word_tokenize(TheHuffingtonPostStr)
TheNewYorkTimesTok = word_tokenize(TheNewYorkTimesStr)
TheVergeTok = word_tokenize(TheVergeStr)

dataTok = word_tokenize(dataStr)
#%%
for line in grouped:
    print(line + "WC = WordCloud().generate("+line+"Str)")
    print("plt.figure()")
    print("plt.imshow("+line+"WC, interpolation='bilinear')")
    print("plt.axis(""off"")")
    print("plt.show()")
    print("#%%")
#%%
ABCNewsWC = WordCloud().generate(ABCNewsStr)
plt.figure()
plt.imshow(ABCNewsWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
AlJazeeraEnglishWC = WordCloud().generate(AlJazeeraEnglishStr)
plt.figure()
plt.imshow(AlJazeeraEnglishWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
BBCNewsWC = WordCloud().generate(BBCNewsStr)
plt.figure()
plt.imshow(BBCNewsWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
BreitbartNewsWC = WordCloud().generate(BreitbartNewsStr)
plt.figure()
plt.imshow(BreitbartNewsWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
CBSNewsWC = WordCloud().generate(CBSNewsStr)
plt.figure()
plt.imshow(CBSNewsWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
CNNWC = WordCloud().generate(CNNStr)
plt.figure()
plt.imshow(CNNWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
DailyMailWC = WordCloud().generate(DailyMailStr)
plt.figure()
plt.imshow(DailyMailWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
FoxNewsWC = WordCloud().generate(FoxNewsStr)
plt.figure()
plt.imshow(FoxNewsWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
IndependentWC = WordCloud().generate(IndependentStr)
plt.figure()
plt.imshow(IndependentWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
MetroWC = WordCloud().generate(MetroStr)
plt.figure()
plt.imshow(MetroWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
MirrorWC = WordCloud().generate(MirrorStr)
plt.figure()
plt.imshow(MirrorWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
NBCNewsWC = WordCloud().generate(NBCNewsStr)
plt.figure()
plt.imshow(NBCNewsWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
ReutersWC = WordCloud().generate(ReutersStr)
plt.figure()
plt.imshow(ReutersWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
TheHillWC = WordCloud().generate(TheHillStr)
plt.figure()
plt.imshow(TheHillWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
TheHuffingtonPostWC = WordCloud().generate(TheHuffingtonPostStr)
plt.figure()
plt.imshow(TheHuffingtonPostWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
TheNewYorkTimesWC = WordCloud().generate(TheNewYorkTimesStr)
plt.figure()
plt.imshow(TheNewYorkTimesWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
TheVergeWC = WordCloud().generate(TheVergeStr)
plt.figure()
plt.imshow(TheVergeWC, interpolation='bilinear')
plt.axis(off)
plt.show()
#%%
ABCNewsfdist =  FreqDist(ABCNewsTok)
print(ABCNewsfdist)
print(ABCNewsfdist.most_common(20))

ABCNewsfdist.plot(20,cumulative=False)
plt.show()
#%%
dataWC = WordCloud().generate(ABCNewsStr)
plt.figure() 
plt.imshow(dataWC, interpolation='bilinear')
plt.axis("off")
plt.show()
#%%
#%%
datafdist =  FreqDist(dataTok)
print(datafdist)
print(datafdist.most_common(20))

datafdist.plot(20,cumulative=False)
plt.show()
#%% Add stop words
stop_words = stopwords.words('english')
stop_words = stop_words + ["(",")","...", "'","‘","?" ,"2","3","4","1",",", "0","90",":", "10", "100", "15", "16", "20", "23", "25", "2nd", "30", "50", "\\r\\n"]

#%% Frequency Dist No stop words
dataTok2 = [i for i in word_tokenize(dataStr.lower()) if i not in stop_words]
#%%
datafdist2 =  FreqDist(dataTok2)
print(datafdist2)
print(datafdist2.most_common(20))

datafdist2.plot(20,cumulative=False)
plt.show()
#%%
dataStrTitle = str(data['description'])
dataTokTitle = [i for i in word_tokenize(dataStrTitle.lower()) if i not in stop_words]
#%%
datafdistTitle =  FreqDist(dataTokTitle)
print(datafdistTitle)
print(datafdistTitle.most_common(20))

datafdistTitle.plot(20,cumulative=False)
plt.show()
#%%
dataWCTitle = WordCloud().generate(dataStrTitle)
plt.figure() 
plt.imshow(dataWCTitle, interpolation='bilinear')
plt.axis("off")
plt.show()
#%% import data from MediaCloud
SECRET_KEY = os.getenv("SECRET_KEY")

mc = mediacloud.api.MediaCloud('SECRET_KEY')
db = mediacloud.storage.MongoStoryDatabase('one_day')
stories = mc.storyList('*', mc.publish_date_query( datetime.date (2020, 01, 01), datetime.date(2020,01,01) ), 
                       last_processed_stories_id=0,rows=100)
[db.addStory(s) for s in stories]
print(db.storyCount())