import urllib.request
from urllib import parse
from urllib.request import Request
import urllib
import csv

from bs4 import BeautifulSoup
import requests
import numpy as np
import nltk
import pandas as pd
nltk.download('punkt')
import re
import csv
import pandas
from nltk.tokenize import sent_tokenize
import os
import csv
from textblob import TextBlob
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

nltk.download('stopwords')

stop_words = stopwords.words('english')




theurl = "https://arynews.tv/"

headers =  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
r = Request(theurl,None, headers)
thepage = urllib.request.urlopen(r)
soup = BeautifulSoup(thepage, "html.parser")

if os.path.exists('AryTemp.csv'):
    os.remove('AryTemp.csv')

def getLinks(theurl):

    thepage = urllib.request.urlopen(r)
    soup = BeautifulSoup(thepage, "html.parser")
    links = []

    for link in soup.ul.findAll('a'):
         if link.text != 'HOME':
             if link.text != 'TV SHOWS':
                 if link.text != 'OFF BEAT':
                     if link.text != 'MULTIMEDIA':
                         if link.text != 'BLOGS':
                            data=[]
                            data.append (link['href']if link['href'].startswith('http') else theurl + link['href'])
                            data.append(link.text)
                            links.append(data)

    return links

def getStories(url):
    r = Request(url[0], None, headers)
    thepage2 = urllib.request.urlopen(r)
    soup = BeautifulSoup(thepage2, "html.parser")
    stories = []

    for story in soup.select('article > div > h2 > a'):
        data =[]
        data.append(story['href'])
        data.append(url[1])
        stories.append(data)
    return stories

#
def getStoryDetails(url):
    r = Request(url[0], None, headers)
    html_page = urllib.request.urlopen(r)
    soup = BeautifulSoup(html_page, "html.parser" )

    title1 = soup.select('div.post-header.post-tp-1-header > h1 > span')[0].get_text()
    news=''
    lines = soup.select(' div.entry-content.clearfix.single-post-content ')
    for line in lines:
        news += line.get_text().replace('\xa0' , '')+' '


    img = soup.select('div.post-header.post-tp-1-header > div.single-featured > img')
    if len(img) > 0:
        img = (img[0]['data-src'])
    else:
        img = ''
    title= [title1 , news , img,url[1]]

    articles = []

    for s in [news]:
        articles.append(sent_tokenize(s))

    for article in articles:
        # print(article)

        word_embeddings = {}
        f = open('glove.6B.100d.txt', encoding='utf-8')

        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            word_embeddings[word] = coefs
        f.close()

        # print(len(word_embeddings))

        clean_article = pd.Series(article).astype(str).str.replace("[^a-zA-Z]", " ")

        clean_article = [s.lower() for s in clean_article]

        # print(clean_article)

        def remove_stopwords(sen):
            sen_new = " ".join([i for i in sen if i not in stop_words])
            return sen_new

        clean_article = [remove_stopwords(r.split()) for r in clean_article]

        # print(clean_article)

        word_embeddings = {}
        f = open('glove.6B.100d.txt', encoding='utf-8')
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            word_embeddings[word] = coefs
        f.close()

        sentence_vectors = []
        for i in clean_article:
            if len(i) != 0:
                v = sum([word_embeddings.get(w, np.zeros((100,))) for w in i.split()]) / (len(i.split()) + 0.001)
            else:
                v = np.zeros((100,))
            sentence_vectors.append(v)

        # print(sentence_vectors)

        sim_mat = np.zeros([len(article), len(article)])



        for i in range(len(article)):
            for j in range(len(article)):
                if i != j:
                    sim_mat[i][j] = \
                    cosine_similarity(sentence_vectors[i].reshape(1, 100), sentence_vectors[j].reshape(1, 100))[0, 0]
                # print(sim_mat[i][j])

        nx_graph = nx.from_numpy_array(sim_mat)
        scores = nx.pagerank(nx_graph)

        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(article)), reverse=True)

        # print(ranked_sentences[0][1])
        mylist = []
        mylist = (ranked_sentences[0][1])

        p = []


        for row in mylist:
            sentence = row
            blob = TextBlob(sentence)
            r = sentence
            if blob.sentiment.polarity == 0:
                p = 'neutral'
            elif blob.sentiment.polarity < 0:
                p = 'negative'
            elif blob.sentiment.polarity > 0:
                p = 'positive'
            my = [r, p]


        with open('AryTemp.csv', 'a+', encoding= 'utf-8-sig') as file:
            writer = csv.writer(file, delimiter=',')
            new = title1, news, img, url[1], mylist, p
            if file.tell()==0:
             writer.writerow(['title', 'news', 'img-url','category','summery','opinion'])
            writer.writerow(new)
            return writer

for item in getLinks("https://dunyanews.tv"):
    for item2 in (getStories(item)):
            print(getStoryDetails(item2))

import os

os.rename('Arytmp.csv', 'ary.csv')





