import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import os

nltk.download('stopwords')
nltk.download('punkt')

def extract_keywords(file_path):
    import matplotlib
    matplotlib.use('Agg')  # Use the 'Agg' backend which does not require a display
    import matplotlib.pyplot as plt
    
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

        # Plot the top keywords
        plt.figure(figsize=(10, 6))
        plt.bar([word[0] for word in top_keywords], [word[1] for word in top_keywords])
        plt.xlabel('Keywords')
        plt.ylabel('Frequency')
        plt.title('Top Keywords')
        
        # Save the plot as an image
        output_folder = 'static/s/barplots'
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, 'top_keywords_barplot.png')
        plt.savefig(output_path)
        plt.close()

        return {
            'top_keywords': top_keywords,
            'barplot_image_path': output_path
        }
