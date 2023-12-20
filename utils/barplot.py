import matplotlib.pyplot as plt
from io import BytesIO
import base64

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

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
