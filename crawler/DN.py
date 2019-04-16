
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import  Request
import csv
import pandas as pd
import numpy as np
import nltk
nltk.download('punkt') # one time execution
import re
import csv
import pandas
from nltk.tokenize import sent_tokenize
import copy
import csv
from textblob import TextBlob
import os

nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx


url = "https://dunyanews.tv/"
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
r = Request(url, None, headers)



thepage = urllib.request.urlopen(r)
soup = BeautifulSoup(thepage, "html.parser" )

if os.path.exists(r'E:\FYP\Dunya\data.csv'):
    os.remove(r'E:\FYP\Dunya\data.csv')
    if os.path.exists(r'E:\FYP\Dunya\DN-summery.csv'):
        os.remove(r'E:\FYP\Dunya\DN-summery.csv')
        if os.path.exists(r'E:\FYP\Dunya\Dunya-News.csv'):
            os.remove(r'E:\FYP\Dunya\Dunya-News.csv')
            if os.path.exists(r'E:\FYP\Dunya\opinion.csv.csv'):
                os.remove(r'E:\FYP\Dunya\opinion.csv.csv')
                if os.path.exists(r'E:\FYP\Dunya\Final-Dunya.csv.csv'):
                    os.remove(r'E:\FYP\Dunya\Final-Dunya.csv.csv')


def getLinks(url):
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page, "html.parser" )
    links = []

    for link in soup.ul.findAll('a'):
        if link.text != 'Featured':
            data = []
            data.append((link['href'] if link['href'].startswith('http') else url + link['href']))
            data.append(link.text)
            links.append(data)

    return links


def getStories(urlstory):
    html_page = urllib.request.urlopen(urlstory[0])
    soup = BeautifulSoup(html_page, "html.parser")
    links = []

    for link in soup.select('article > h3 > a'):
        data=[]

        data.append((link['href'] if link['href'].startswith('http') else url + link['href']))
        data.append(urlstory[1])
        links.append(data)

    return links

def getStoryDetails(url):
    html_page = urllib.request.urlopen(url[0])
    soup = BeautifulSoup(html_page, "html.parser" )


    title =soup.select('#main-heading > div.date > h2')[0].get_text()     #ppppppheading
    news =soup.select('#post_content > article > div.post_content ')[0].get_text()

    img = soup.select('#post_content > article > div.pic.post_thumb > img')
    if  len(img) > 0:
     img=(img[0]['src'])
    else:
     img = ''
    articles = []

    for s in [news]:
        articles.append(sent_tokenize(s))

    # articles = [y for x in articles for y in x]

    for article in articles:
        # print(article)

        # Extract word vectors
        word_embeddings = {}
        f = open('glove.6B.100d.txt', encoding='utf-8')
        for line in f:
            values = line.split()
            word = values[0]
            coefs = np.asarray(values[1:], dtype='float32')
            word_embeddings[word] = coefs
        f.close()

        clean_article = pd.Series(article).astype(str).str.replace("[^a-zA-Z]", " ")
        # make alphabets lowercase
        clean_article = [s.lower() for s in clean_article]

        # print(clean_article)

        # function to remove stopwords
        def remove_stopwords(sen):
            sen_new = " ".join([i for i in sen if i not in stop_words])
            return sen_new

        # remove stopwords from the articles
        clean_article = [remove_stopwords(r.split()) for r in clean_article]

        # print(clean_article)

        # Extract word vectors
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

        # similarity matrix
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

        # print(ranked_sentences[0][1]
        mylist=[]
        mylist = ranked_sentences[0][1]

        p = []
        rows = mylist
        for row in rows:
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

        with open(r'E:\FYP\Dunya\dunya.csv', 'a+', encoding= 'utf-8-sig') as file:
            writer = csv.writer(file, delimiter=',')
            if file.tell()==0:
             writer.writerow(['title', 'news', 'img-url' , 'category' , 'summery' , 'opinion'])
            writer.writerow([title,news,img,url[1],mylist,p])
            return writer

for item in getLinks("https://dunyanews.tv"):
    for item2 in (getStories(item)):
            print(getStoryDetails(item2))


