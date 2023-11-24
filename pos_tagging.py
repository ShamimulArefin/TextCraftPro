import nltk

nltk.download('averaged_perceptron_tagger')

def pos_tag_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(words)
        return pos_tags
