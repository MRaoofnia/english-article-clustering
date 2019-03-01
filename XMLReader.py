import requests
from Article import Article

class Reader:
    articles = []
    
    def __init__(self):
        id = 1
        URL = "http://jad.shahroodut.ac.ir/"
        for counter in range(200): 
            PARAMS = {'_action':'xml','article':id} 
            req = requests.get(url = URL, params = PARAMS)
            result = self.parse_xml(req.text)
            print(req.text)
            if result != None:
                counter = 1
                self.articles.append(result)
                print(result)
            else:
                print(PARAMS)
                print('empty url')
            id += 1

    def parse_xml(self, context):
        if 'Journal' in context: #to check if url contains an XML with article
            abstract = context[context.index("<Abstract>")+10:context.index("</Abstract>")]
            title = context[context.index("<ArticleTitle>")+10:context.index("</ArticleTitle>")]
            return Article(abstract, title)
        else:
            return None
