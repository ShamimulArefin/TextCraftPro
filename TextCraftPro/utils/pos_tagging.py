import nltk

nltk.download('averaged_perceptron_tagger')

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