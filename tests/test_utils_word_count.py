import os
from TextCraftPro.utils.word_count import count_words

SAMPLE_FILE_PATH = os.path.join(os.path.dirname(__file__), 'sample.txt')

def test_count_words():
    # Create a sample text file for testing
    with open(SAMPLE_FILE_PATH, 'w', encoding='utf-8') as file:
        file.write("This is a sample text. It has words and sentences. Let's count them.")

    # Test the count_words function
    result = count_words(SAMPLE_FILE_PATH)
    
    # Clean up the sample file after testing
    os.remove(SAMPLE_FILE_PATH)

    # Check the expected counts
    assert result['Words'] == 13
    assert result['Sentences'] == 3
    assert result['Paragraphs'] == 1
    assert result['Characters'] == 68  # Counting spaces and punctuation