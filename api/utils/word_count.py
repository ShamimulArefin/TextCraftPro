def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)
