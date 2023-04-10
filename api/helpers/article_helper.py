from newspaper import Article
from newspaper import Config

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Unique/97.7.2876.77"
ARTICLE_TIMEOUT = 10

##########CONFIG##################
config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = ARTICLE_TIMEOUT
###################################

def get_content(url):
    article = Article(url)
    article.download()
    article.parse()
    
    return article.text