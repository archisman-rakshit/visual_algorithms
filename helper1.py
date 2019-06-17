import networkx as nx
import matplotlib.pyplot as plt
import sys
from PIL import Image
def helper():
        G = nx.Graph()
        f = open('%s'%(sys.argv[1]))        
        n = int(f.readline())
        wtMatrix = []
        for i in range(n):
                list1 = list(map(int, (f.readline()).split()))
                wtMatrix.append(list1)
       
        for i in range(n) :
                for j in range(n)[i:] :
                        if wtMatrix[i][j] > 0 :
                                G.add_edge(i, j, length = wtMatrix[i][j])
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels = True) 
        edge_labels = nx.get_edge_attributes(G,'length')
        nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11)   
        plt.savefig('abc.png')
        image=Image.open('abc.png')
        image.show()         
if __name__ == "__main__":
        helper()