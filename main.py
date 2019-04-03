from Article import Article
from XMLReader import Reader
import math
import json

def max(sims):
    max = 0
    ij = {'i':0, 'j':0}
    for i in range(len(sims)):
        for j in range(i):
            if sims[i][j] > max:
                max = sims[i][j]
                ij = {'i':i, 'j':j}
    return ij

def cluster(inpath, inthreshold):
    print("reading articles from web...")
    reader = Reader() #Reader reads all XML documents from 'jad' and returns an array of articles
    articles = reader.articles #Article class tokenizes and lemmatizes tokens itself
    
    print("calculating idfs...")
    wordsdf = {}
    for article in articles: #finding dfs
        tfmap = {}
        tfmap = article.tf
        for word in tfmap:
            if word in wordsdf:
                wordsdf[word] += 1
            else:
                wordsdf[word] = 1
    
    wordsidf = {}
    for word in wordsdf: #finding idfs
        wordsidf[word] = math.log(len(articles)/wordsdf[word], 2)
    
    for article in articles: #setting tfidfs
        for word in article.tf:
            article.tfidf[word] = article.tf[word] * wordsidf[word]
    
    print("calculating cosine similarities...")
    #now clustering -----------------------------------------------
    #calculating cosine similarity
    similarities = []
    for i in range(len(articles)):
        similarities.append([])
        a = articles[i]
        for j in range(len(articles)):
            b = articles[j]
            similarity = 0
            for word in b.tfidf:
                if word in a.tfidf:
                    similarity += a.tfidf[word] * b.tfidf[word]
            similarity = similarity / (a.vectorlength * b.vectorlength)
            similarities[i].append(similarity)
        similarities[i][i] = 0

    print("clustering...")
    flag = 1
    for article in articles:
        article.flag = flag
        flag += 1

    threshold = inthreshold
    if threshold == 0:
        threshold = 550

    while similarities[max(similarities)['i']][max(similarities)['j']] > threshold:
        ij = max(similarities)
        i = ij['i']
        j = ij['j']
        currentflag = articles[j].flag
        for iterator in range(len(articles)):
            if articles[iterator].flag == articles[i].flag:
                articles[iterator].flag = articles[j].flag
        similarities[i][j] = 0
        similarities[j][i] = 0

    print("making clusters")
    clusters = []
    while flag > 0:
        currentcluster = []
        for article in articles:
            if article.flag == flag:
                currentcluster.append(article)
        if len(currentcluster) > 0:
            clusters.append(currentcluster)
        flag -= 1

    print(clusters)
    serializableClusters = []
    for cl in clusters:
        templc = []
        for artic in cl:
            templc.append(artic.todict())
        serializableClusters.append(templc)

    with open(inpath + '/' + "output.json", "w") as f:
        f.write(json.dumps(serializableClusters, ensure_ascii=False, indent=4))



if __name__ == "__main__":
    cluster()
