from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
from .pieplot import *

def analyze_sentiment(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        sid = SentimentIntensityAnalyzer()
        sentiment_score = sid.polarity_scores(text)

        # Classify sentiment based on the compound score
        if sentiment_score['compound'] >= 0.05:
            sentiment = 'Positive'
        elif sentiment_score['compound'] <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        # get sentiment pie plot
        plot = get_plot(sentiment_score)
        
        return {
            'Sentiment Score': sentiment_score,
            'Sentiment': sentiment,
            'sentimentPie':plot
        }
