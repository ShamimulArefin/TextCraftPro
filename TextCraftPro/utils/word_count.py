import re

def count_words(file_path):
    word_count = 0
    paragraph_count = 0
    sentence_count = 0
    character_count = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

        # # Count words
        word_count = len(re.findall(r'\b\w+(?:\'\w+)?(?:-\w+)?\b', text))
        
        # # Count sentences
        sentence_count = len(re.findall(r'[.!?]+', text))

        # # Count paragraphs (assumes paragraphs are separated by two or more line breaks)
        paragraph_count = len(re.findall(r'\n\s*\n', text)) + 1  # Adding 1 for the last paragraph

        # # Count characters (including spaces and punctuation)
        character_count = len(text)

        count_dict = {
            'Words': word_count,
            'Sentences': sentence_count,
            'Paragraphs': paragraph_count,
            'Characters': character_count
        }

        return count_dict