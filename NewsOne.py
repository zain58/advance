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
nltk.download('punkt') # one time execution
import re
import csv
import pandas
from nltk.tokenize import sent_tokenize
import copy
import csv
import os
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx



theurl = "https://www.newsone.tv/"

headers =  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
r = Request(theurl,None, headers)
thepage = urllib.request.urlopen(r)
soup = BeautifulSoup(thepage, "html.parser")

if os.path.exists('NewsOnetemp.csv'):
    os.remove('NewsOnetemp.csv')
if os.path.exists('newsone.csv'):
    os.remove('newsone.csv')

def getLinks(theurl):
    thepage = urllib.request.urlopen(r)
    soup = BeautifulSoup(thepage, "html.parser")
    links = []

    for link in soup.ul.findAll('a'):
        if link.text != ' Home':
             if link.text != ' Latest News':
                if link.text != 'Blogs ':
                    if link.text != 'PSL 2019':
                         if link.text != 'Opinions':
                             if link.text != 'Multimedia ':
                                 if link.text != 'Documentaries':
                                     if link.text != 'Packages':
                                         if link.text != 'Headlines':
                                             if link.text != 'Viral Videos':
                                                 if link.text != "Shows":
                                                     if link.text != "Urdu":
                                                         data=[]
                                                         data.append (link['href']if link['href'].startswith('http') else theurl + link['href'])

                                                         data.append(link.text)
                                                         print(link.text)
                                                         links.append(data)
    return links

def getStories(url):
    thepage2 = urllib.request.urlopen(url[0])
    soup = BeautifulSoup(thepage2, "html.parser")
    stories = []

    for story in soup.select('.post-block > div.summary > h2 > a'):
        data=[]
        data.append(story['href'])
        data.append(url[1])
        stories.append(data)

    return stories

def getStoryDetails(url):
    html_page = urllib.request.urlopen(url[0])
    soup = BeautifulSoup(html_page, "html.parser" )

    title =soup.select('#masonry-container > div.spacer > div > div > div.col-sm-9.col-xs-12.single-page-tem > section > div > div.page-title > h1')[0].get_text()                     #masonry-container > div.spacer > div > div > div.col-sm-9.col-xs-12.single-page-tem > section > div > div.page-title > h1

    news = ''
    lines =soup.select('#sigle-story  p')
    for line in lines:

        news += line.get_text().replace('“','').replace('”','').replace('\xa0' , '')+' '
    # print(news)



    img = soup.select('#masonry-container > div.spacer > div > div > div.col-sm-9.col-xs-12.single-page-tem > section > div > div.single-post > div.post-content > div.post-thumb-single > img')

    if  len(img) > 0:
     img=(img[0]['src'])
    else:
     img = ''

    # new = [title, news, img, url[1]]
    # return new

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
                        cosine_similarity(sentence_vectors[i].reshape(1, 100), sentence_vectors[j].reshape(1, 100))[
                            0, 0]
                # print(sim_mat[i][j])

        nx_graph = nx.from_numpy_array(sim_mat)
        scores = nx.pagerank(nx_graph)

        ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(article)), reverse=True)
        mylist = []
        # print(ranked_sentences[0][1])
        mylist = ranked_sentences[0][1]
        p = []


        from textblob import TextBlob
        for sentence in mylist[0]:
            row = sentence
            row = mylist
            blob = TextBlob(row)
            # r = sentence
            if blob.sentiment.polarity == 0:
                p = 'neutral'
            elif blob.sentiment.polarity < 0:
                p = 'negative'
            elif blob.sentiment.polarity > 0:
                p = 'positive'
        # print(blob.sentiment.polarity)
        print(p)


        with open('NewsOnetemp.csv', 'a+', encoding='utf-8-sig') as file:
            writer = csv.writer(file, delimiter=',')
            new = title, news, img, url[1], mylist, p
            if file.tell() == 0:
                writer.writerow(['title', 'news', 'img-url', 'category', 'summery', 'opinion'])
            writer.writerow(new)
            return writer

for item in getLinks("https://www.newsone.tv/"):
    counter=0
    for item2 in (getStories(item)):
            print(counter)
            if(counter>0):
                print(getStoryDetails(item2))
            counter=counter+1
import os
os.rename('NewsOnetemp.csv', 'newsone.csv')







