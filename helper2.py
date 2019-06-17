import networkx as nx
import matplotlib.pyplot as plt
import sys
from PIL import Image
def helper():
    G = nx.DiGraph()
    f = open('dijkstrainput.txt')
    n = int(f.readline())
    wtMatrix = []
    for i in range(n):
        list1 = list(map(int, (f.readline()).split()))
        wtMatrix.append(list1)
    source = int(f.readline())  
    for i in range(n) :
        for j in range(n) :
            if wtMatrix[i][j] > 0 :
                G.add_edge(i, j, length = wtMatrix[i][j]) 
    pos = nx.shell_layout(G)
    nx.draw(G, pos, with_labels = True)  
    edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11)  
    plt.savefig('abc.png')
    image=Image.open('abc.png')
    image.show()         
if __name__ == "__main__":
    helper()