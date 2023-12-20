import os
from TextCraftPro.utils.pos_tagging import pos_tag_text

SAMPLE_FILE_PATH = os.path.join(os.path.dirname(__file__), 'sample.txt')

def test_pos_tag_text():
    with open(SAMPLE_FILE_PATH, 'w') as file:
        file.write("This is a sample text for part-of-speech tagging.")

    # Test the pos_tag_text function
    result = pos_tag_text(SAMPLE_FILE_PATH)

     # Clean up the sample file after testing
    os.remove(SAMPLE_FILE_PATH)

    # Check that the expected part-of-speech tags are a subset of the actual result
    expected_tags = {'DT': ['This', 'a'], 'VBZ': ['is'], 'JJ': ['sample', 'part-of-speech'], 'NN': ['text', 'tagging'], 'IN': ['for'], '.': ['.']}
    
    assert result == expected_tags
