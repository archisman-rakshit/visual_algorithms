import networkx as nx
import matplotlib.pyplot as plt
import sys,os,time
from tkinter import messagebox
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


def minDistance(dist, mstSet, V):
   	min = inf #assigning largest numeric value to min
   	for v in range(V):
   		if mstSet[v] == False and dist[v] < min:
   			min = dist[v]
   			min_index = v
   	return min_index




def prims(G, pos):
	V = len(G.nodes()) 
	dist = [] 
	parent = [None]*V 
	mstSet = [] 
	
	for i in range(V):
		dist.append(inf)
		mstSet.append(False)
	dist[0] = 0
	parent[0]= -1
	str1=prt(dist)
	str2=prt(parent)
	str3="INITIALLY\n"+"\nMst_Set is Empty\n"+"\nKEY_Value\n"+str1+"\nParent Table\n"+str2
	master = tk.Tk()
	master.title("Simple Prog")
	msg = tk.Message(master, text = str3)
	msg.config(bg='lightblue', font=('times', 16))
	msg.pack()
	def ask_quit():
		master.destroy()
	ret_val=messagebox.showinfo("Alert","Press X / Ok to Close Calculation Window")
	if (ret_val == "ok"):	
		ask_quit()	
		
	for count in range(V-1):
		u = minDistance(dist, mstSet, V) #pick the minimum distance vertex from the set of vertices
		mstSet[u] = True
		str5="\nMinimum distance vertex picked from the set of vertices is "+ str(u)+"\n"
		for v in range(V):
			if (u, v) in G.edges():
				if mstSet[v] == False and G[u][v]['length'] < dist[v]:
					dist[v] = G[u][v]['length']
					parent[v] = u
		str3=prt(dist)
		str4=prt(parent)
		str6=prt1(mstSet)
		str7=str5+"\nMst_Set is\n"+str6+"\nKEY_Value\n"+str3+"\nParent Table\n"+str4
		master = tk.Tk()
		master.title("Simple Prog")
		msg = tk.Message(master, text = str7)
		msg.config(bg='lightblue', font=('times', 16))
		msg.pack()
		def ask_quit():
			master.destroy()
		ret_val=messagebox.showinfo("Alert","Press X / Ok to Close Calculation Window")
		if (ret_val == "ok"):	
			ask_quit()			
	
	for X in range(V):
		if parent[X] != -1: #ignore the parent of the starting node
			if (parent[X], X) in G.edges():				
				#plt.waitforbuttonpress()
				#plt.pause(0.5)
				nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = 'r')
				
	plt.show()
	return




def CreateGraph():
	G = nx.Graph()
	f = open('primsinput.txt')
	n = int(f.readline())
	wtMatrix = []
	for i in range(n):
		list1 = list(map(int, (f.readline()).split()))
		wtMatrix.append(list1)
	
	for i in range(n) :
		for j in range(n)[i:] :
			if wtMatrix[i][j] > 0 :
					G.add_edge(i, j, length = wtMatrix[i][j]) 
	return G

def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  
	edge_labels = nx.get_edge_attributes(G,'length')
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) 
	return pos




if __name__ == "__main__":
	image=Image.open('PRIM.jpg')
	image.show()
	time.sleep(5)
	cmd="primsinput.txt"
	os.system('helper1.py %s'% (cmd))	
	G = CreateGraph()
	pos = DrawGraph(G)
	print(pos)
	prims(G, pos)
	#plt.show()
