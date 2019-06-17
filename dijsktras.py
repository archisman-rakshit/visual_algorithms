import networkx as nx
import matplotlib.pyplot as plt
import os,sys,time
from tkinter import messagebox
from tkinter import *
import tkinter as tk
from PIL import Image

inf = float('inf')

def prt1(lis):
	V=len(lis)
	str4="{  "
	for j in range(V):
		strx=str(lis[j])
		if(strx=="True"):
			str4=str4+str(j)+" , "

	str4=str4[:-2]+" }\n"
	return str4

def prt(lis):
	V=len(lis)
	str4=""
	for i in range(2):
		for j in range(V):
			if( i == 0):
				str4=str4+str(j)+"\t"
			else:
				str4=str4+str(lis[j])+"\t"
		str4=str4+"\n"

	return str4

def minDistance(dist, sptSet, V):
   	min = inf 
   	for v in range(V):
   		if sptSet[v] == False and dist[v] <= min:
   			min = dist[v]
   			min_index = v
   			return min_index




def dijsktras(G, source, pos):
	V = len(G.nodes()) 
	dist = [] 
	parent = [None]*V 
	sptSet = [] 
	for i in range(V):
		dist.append(inf)
		sptSet.append(False)
	dist[source] = 0
	parent[source]= -1 
	str2=prt(dist)
	str3="INITIALLY\n"+"\nspt_Set is Empty\n"+"\nDistance Table\n"+str2+"\n"
	master = tk.Tk()
	master.title("Simple Prog")
	msg = tk.Message(master, text = str3)
	msg.config(bg='lightblue', font=('times', 18))
	msg.pack()
	def ask_quit():
		master.destroy()
	ret_val=messagebox.showinfo("Alert","Press X / Ok to Close Calculation Window")
	if (ret_val == "ok"):	
		ask_quit()		
	
	for count in range(V-1):
		u = minDistance(dist, sptSet, V) 
		sptSet[u] = True
		
		for v in range(V):
			if (u, v) in G.edges():
				if sptSet[v] == False and dist[u] != inf and dist[u] + G[u][v]['length'] < dist[v]:
					dist[v] = dist[u] + G[u][v]['length']
					parent[v] = u
		str3=prt1(sptSet)
		str4=prt(dist)
		str5=prt(parent)
		str6="\nspt_Set is \n"+str3+"\nDistance table\n"+str4+"\nParent Table\n"+str5
		master = tk.Tk()
		master.title("Simple Prog")
		msg = tk.Message(master, text = str6)
		msg.config(bg='lightblue', font=('times', 16))
		msg.pack()
		def ask_quit():
			master.destroy()
		ret_val=messagebox.showinfo("Alert","Press X / Ok to Close Calculation Window")
		if (ret_val == "ok"):	
			ask_quit()		
		
		
	for X in range(V):
		if parent[X] != -1: #ignore the parent of root node 
			if (parent[X], X) in G.edges():
				#plt.waitforbuttonpress()
				#plt.pause(0.5)
				nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = 'r')
	return



#takes input from the file and creates a weighted graph
def CreateGraph():
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
	return G, source




def DrawGraph(G):
	pos = nx.shell_layout(G)
	nx.draw(G, pos, with_labels = True)  
	edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) 
	return pos



#main function
if __name__ == "__main__":
	#image=Image.open('DIJ.jpg')
	#image.show()
	#time.sleep(5)	
	cmd="dijkstrainput.txt"
	os.system('helper2.py %s'% (cmd))
	G,source = CreateGraph()
	pos = DrawGraph(G)
	dijsktras(G, source, pos)
	plt.show()

