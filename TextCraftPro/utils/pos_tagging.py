import nltk

nltk.download('averaged_perceptron_tagger')

"""
POS Tagging of Text
This function reads text from a file, tokenizes it, and performs Part-of-Speech (POS) tagging using NLTK.

param file_path: The path to the text file.
return: A dictionary where keys are POS tags and values are lists of words with the corresponding tag.
"""
def pos_tag_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = nltk.word_tokenize(text)
        pos_tags = nltk.pos_tag(words)

        pos_dict = {}
        
        for word, tag in pos_tags:
            if tag in pos_dict:
                if word not in pos_dict[tag]:
                    pos_dict[tag].append(word)
            else:
                pos_dict[tag] = [word]

        return pos_dict