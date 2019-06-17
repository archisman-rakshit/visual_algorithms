import networkx as nx
import matplotlib.pyplot as plt
import sys,os,time
from tkinter import messagebox
import tkinter as tk
from PIL import Image

inf = float('inf')

def prt(lis):
	V=len(lis)
	str4="\t"
	for i in range(2):
		for j in range(V):
			if( i == 0):
				str4=str4+str(j)+"\t"
			else:
				str4=str4+str(lis[j])+"\t"
		if( i == 0):
			str4=str4+"\n"+"dist\t"
		else:
			str4=str4+"\n"
		
	return str4

def prt1(lis):
	V=len(lis)
	str4="\t"
	for i in range(2):
		for j in range(V):
			if( i == 0):
				str4=str4+str(j)+"\t"
			else:
				str4=str4+str(lis[j])+"\t"
		if( i == 0):
			str4=str4+"\n"+"parent\t"
		else:
			str4=str4+"\n"
		
	return str4
 
def bellmanFord(G, source, pos):
	V = len(G.nodes()) 
	dist = [] 
	parent = [None]*V 
	for i in range(V):
		dist.append(inf)

	parent[source] = -1; 
	dist[source] = 0;
	str5=prt(dist)
	str9=prt1(parent)

	for i in range(V-1):
		for u, v, d in G.edges(data = True):
			if dist[u] + d['length'] < dist[v]: 
				str3=str(dist[u])+" + "+str(d['length']) +" < "+ str(dist[v])
				dist[v] = d['length'] + dist[u]
				parent[v] = u
				str2=' , '.join(str(e) for e in parent)
				str1=' , '.join(str(e) for e in dist)
				str3="Iteration no "+str(i+1)+"\nEdge Selected "+str(u)+" -> "+str(v)+"\n"+str3+"\n"
				str7=prt(dist)
				str8=prt1(parent)
				str6=str3+"PREVIOUS Distance table\n"+str5+"\nNEW Distance Table\n"+str7+"\nPREVIOUS Parent table\n"+str9+"\nNEW Parent table\n"+str8
				str5=str7
				str9=str8
				master = tk.Tk()
				master.title("Simple Prog")
				msg = tk.Message(master, text = str6)
				msg.config(bg='lightblue', font=('times', 20))
				msg.pack()
				def ask_quit():
					master.destroy()
				ret_val=messagebox.showinfo("Alert","Press X / Ok to Close Calculation Window")
				if (ret_val == "ok"):	
					ask_quit()	
	for u, v, d in G.edges(data = True):
		if dist[u] + d['length'] < dist[v]:
			master = tk.Tk()
			master.title("Simple Prog")
			msg = tk.Message(master, text = "Negetive Cycle Detected")
			msg.config(bg='lightblue', font=('times', 20))
			msg.pack()			
			
	for v in range(V):
		if parent[v] != -1: 
			if (parent[v], v) in G.edges():
				#plt.waitforbuttonpress()
				#plt.pause(0.5)
				nx.draw_networkx_edges(G, pos, edgelist = [(parent[v], v)], width = 2.5, alpha = 0.6, edge_color = 'r')
	return

def createGraph():
	G = nx.DiGraph()
	f = open('bellmaninput.txt')
	n = int(f.readline())
	wtMatrix = []
	for i in range(n):
		list1 = list(map(int, (f.readline()).split()))
		wtMatrix.append(list1)
	source = int(f.readline()) 
	for i in range(n) :
		for j in range(n) :
			if wtMatrix[i][j] != 0 :
					G.add_edge(i, j, length = wtMatrix[i][j])
	return G, source



def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  
	edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11)
	return pos



if __name__ == "__main__":
	image=Image.open('Bellman-Ford-Algorithm.jpg')
	image.show()
	time.sleep(5)
	cmd="bellmaninput.txt"
	os.system('helper3.py %s'% (cmd))
	G, source = createGraph()
	pos = DrawGraph(G)
	bellmanFord(G, source, pos)
	plt.show()
