from newsapi import NewsApiClient
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_stock_news(stock_symbol, api_key):
    """
    Fetch the latest news for a stock from the NewsAPI.
    
    Parameters:
        stock_symbol (str): The stock symbol to search news for.
        api_key (str): Your NewsAPI key.
        
    Returns:
        list: A list of news articles.
    """
    newsapi = NewsApiClient(api_key= "8d1de582f15a43878a512849bc1abb7e")
    articles = newsapi.get_everything(q=stock_symbol, language="en", sort_by="relevancy")
    return articles['articles']

def analyze_sentiment(news_articles):
    """
    Analyze sentiment of the news articles.
    
    Parameters:
        news_articles (list): A list of news articles.
        
    Returns:
        list: A list of sentiment scores for each article.
    """
    sid = SentimentIntensityAnalyzer()
    sentiments = []
    for article in news_articles:
        score = sid.polarity_scores(article['title'])
        sentiments.append({'Title': article['title'], 'Sentiment': score['compound']})
    return sentiments
