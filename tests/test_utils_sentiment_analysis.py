import os
from TextCraftPro.utils.sentiment_analysis import analyze_sentiment

SAMPLE_FILE_PATH = os.path.join(os.path.dirname(__file__), 'sample.txt')

def test_analyze_sentiment_positive():
    with open(SAMPLE_FILE_PATH, 'w') as file:
        file.write("This is a positive statement.")

    # Test the analyze_sentiment function
    result = analyze_sentiment(SAMPLE_FILE_PATH)

    # Clean up the sample file after testing
    os.remove(SAMPLE_FILE_PATH)

    # Check the expected sentiment
    assert result['Sentiment'] == 'Positive'

def test_analyze_sentiment_negative():
    with open(SAMPLE_FILE_PATH, 'w') as file:
        file.write("This is a negative statement.")

    # Test the analyze_sentiment function
    result = analyze_sentiment(SAMPLE_FILE_PATH)

     # Clean up the sample file after testing
    os.remove(SAMPLE_FILE_PATH)

    # Check the expected sentiment
    assert result['Sentiment'] == 'Negative'

def test_analyze_sentiment_neutral():
    with open(SAMPLE_FILE_PATH, 'w') as file:
        file.write("This is a neutral statement.")

    # Test the analyze_sentiment function
    result = analyze_sentiment(SAMPLE_FILE_PATH)
        
    # Clean up the sample file after testing
    os.remove(SAMPLE_FILE_PATH)

    # Check the expected sentiment
    assert result['Sentiment'] == 'Neutral'