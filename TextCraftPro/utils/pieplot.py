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
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

"""
Generates a pie chart plot from sentiment scores and returns
the plot as a base64-encoded string.
    
Args:
sentiment_score (dict): A dictionary containing sentiment scores.
"""
def get_plot(sentiment_score):
    plt.switch_backend('AGG')
    ingredients = list(sentiment_score.keys())
    data = list(sentiment_score.values())
    # Ensure non-negative values for the pie chart
    data = [max(0, value) for value in data]
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))
    wedges, texts, autotexts = ax.pie(data, autopct='%1.1f%%',
                                  textprops=dict(color="w"))
    ax.legend(wedges, ingredients,
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=8, weight="bold")
    plt.tight_layout()
    graph = get_graph()
    return graph
