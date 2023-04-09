from newspaper import Article

def get_content(url):
    article = Article(url)
    article.download()
    article.parse()
    
    return article.text