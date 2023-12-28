import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('stopwords')
nltk.download('punkt')

from .barplot import *

"""
Extracts the top keywords and their frequencies from a text file.

Parameters:
    - file_path (str): The path to the input text file.

Returns:
    - dict: A dictionary containing the top keywords and a bar plot.
"""
def extract_keywords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # Tokenize the text
        words = word_tokenize(text)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

        # Calculate word frequencies
        word_freq = Counter(filtered_words)

        # Get the top N keywords
        top_keywords = word_freq.most_common(10)

        # get barplot using topkeywords
        barplot = get_plot(top_keywords)

        return {
            'top_keywords': top_keywords,
            'barplot': barplot
        }
