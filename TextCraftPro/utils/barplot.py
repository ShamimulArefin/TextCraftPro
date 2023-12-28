import matplotlib.pyplot as plt
from io import BytesIO
import base64

"""
Generates a graph image from the current Matplotlib figure and 
returns it as a base64-encoded string (decoding to utf-8 for html).
"""
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png) # Encode the PNG image bytes in base64
    graph = graph.decode('utf-8') # Decode the base64 bytes to UTF-8 for use in HTML
    buffer.close()
    return graph

"""
    Generates a bar plot of the top keywords and returns it as a base64-encoded string.
    Args:
        top_keywords (list): A list of tuples containing top keywords and their counts.
"""
def get_plot(top_keywords):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Top Keywords')
    plt.bar([word[0] for word in top_keywords], [word[1] for word in top_keywords])
    plt.xlabel('Words')
    plt.ylabel('Counts')
    plt.tight_layout()
    graph = get_graph()
    return graph
