import os
from TextCraftPro.utils.keyword_extraction import extract_keywords

SAMPLE_FILE_PATH = os.path.join(os.path.dirname(__file__), 'sample.txt')

def test_extract_keywords():
    with open(SAMPLE_FILE_PATH, 'w', encoding='utf-8') as file:
        file.write("This is a sample text for keyword extraction. It contains some repeated words for testing.")

    # Test the extract_keywords function
    result = extract_keywords(SAMPLE_FILE_PATH)

    # Clean up the sample file after testing
    os.remove(SAMPLE_FILE_PATH)

    # Check the expected top keywords
    expected_top_keywords = [('sample', 1), ('text', 1), ('keyword', 1), ('extraction', 1), ('contains', 1), ('repeated', 1), ('words', 1), ('testing', 1)]
    
    assert result['top_keywords'] == expected_top_keywords