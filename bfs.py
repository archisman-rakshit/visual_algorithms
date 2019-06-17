import networkx as nx
import matplotlib.pyplot as plt
from tkinter import messagebox
from tkinter import *
import os
import time
from PIL import Image


#BFS traversal 
def BFS(G, source, pos): 
	visited = [False]*(len(G.nodes()))
	queue = []
	queue.append(source)
	visited[source] = True
	str1=' , '.join(str(e) for e in visited)
	str2=' , '.join(str(e) for e in queue)
	messagebox.showinfo("Initial Tables","queue :  { "+str2+" }\n\nVisted :\n{ "+str1+" }")
	while queue:
		curr_node = queue.pop(0)
		print(curr_node)
		for i in G[curr_node]:  #iterates through all the possible vertices adjacent to the curr_node
			if visited[i] == False:
				queue.append(i)
				visited[i] = True
				str3=' , '.join(str(e) for e in visited)
				str4=' , '.join(str(e) for e in queue)
				messagebox.showinfo("Initial Tables","Current node Selected: "+str(curr_node)+ "\nqueue :  { "+str4+" }\n\nVisted :\n{ "+str3+" }")
				nx.draw_networkx_edges(G, pos, edgelist = [(curr_node,i)], width = 2.5, alpha = 0.6, edge_color = 'r')
				#plt.waitforbuttonpress()
				plt.pause(1)
				
	return



#takes input from the file and creates a weighted graph
def CreateGraph():
	G = nx.DiGraph()
	f = open('bfsinput.txt')
	n = int(f.readline())
	wtMatrix = []
	for i in range(n):
		list1 = list(map(int, (f.readline()).split()))
		wtMatrix.append(list1)
	source = int(f.readline()) #source vertex from where BFS has to start
	#Adds egdes along with their weights to the graph 
	for i in range(n):
		for j in range(n):
			if wtMatrix[i][j] > 0:
					G.add_edge(i, j, length = wtMatrix[i][j]) 
	return G, source



#draws the graph and displays the weights on the edges
def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
	edge_labels = dict([((u,v,), d['length']) for u, v, d in G.edges(data = True)])
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) #prints weight on all the edges
	return pos



#main function
if __name__== "__main__":
	image=Image.open('BFS_1.jpg')
	image.show()
	image=Image.open('BFS_2.jpg')
	image.show()
	time.sleep(5)
	cmd="bfsinput.txt"
	os.system('helper.py %s'% (cmd))
	G,source = CreateGraph()
	pos = DrawGraph(G)
	BFS(G, source, pos)
	plt.show()

