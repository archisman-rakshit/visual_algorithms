import networkx as nx
import matplotlib.pyplot as plt
import sys
from PIL import Image
def helper():
    H= nx.DiGraph()
    f = open('%s'%(sys.argv[1]))
    n = int(f.readline())
    wtMatrix = []
    for i in range(n):
        list1 = list(map(int, (f.readline()).split()))
        wtMatrix.append(list1)
    source = int(f.readline()) 
    for i in range(n) :
        for j in range(n) :
            if wtMatrix[i][j] != 0 :
                H.add_edge(i, j, weight = wtMatrix[i][j])
    po=nx.spring_layout(H)
    nx.draw(H,po,with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(H,'weight')
    nx.draw_networkx_edge_labels(H,po,edge_labels=labels)
    plt.savefig('abc.png')
    image=Image.open('abc.png')
    image.show()    
if __name__ == "__main__":
    helper()