import matplotlib.pyplot as plt
import networkx as nx 
import sys
from tkinter import messagebox
from tkinter import *
import os
import time
from PIL import Image

def getMin(G,mstFlag):
	min=sys.maxsize
	for i in [(u,v,edata['length']) for u,v,edata in G.edges(data=True) if 'length' in edata]:
		if mstFlag[i]==False and i[2]<min:
			min=i[2]
			min_edge=i
	return min_edge

def findRoot(parent,i):
	if parent[i]==i:
		return i
	return findRoot(parent,parent[i])

def union(parent,order,x,y):
	xroot=findRoot(parent,x)
	yroot=findRoot(parent,y)
	if(order[xroot] < order[yroot]):
		parent[xroot]=yroot
	elif(order[yroot] < order[xroot]):
		parent[yroot]=xroot
	else:
		parent[yroot]=xroot
		order[xroot]+=1

def kruskals(G,pos):
	eLen=len(G.edges())
	vLen=len(G.nodes())
	cost=0
	mst=[]
	mstFlag={}
	for i in [(u,v,edata['length']) for u,v,edata in G.edges(data=True) if 'length' in edata]:
		mstFlag[i]=False
	parent=[None]*vLen
	order=[None]*vLen
	for v in range(vLen):
		parent[v]=v
		order[v]=0
	while len(mst) < vLen-1 :
		curr_edge=getMin(G,mstFlag)
		mstFlag[curr_edge]=True
		y=findRoot(parent,curr_edge[1])
		x=findRoot(parent,curr_edge[0])
		if x!=y:
			mst.append(curr_edge)
			union(parent,order,x,y)
	for X in mst:
		if (X[0],X[1]) in G.edges():
			
			#plt.waitforbuttonpress()
			i=X[0]
			j=X[1]
			sc=wtmatrix[i][j]
			cost=cost+wtmatrix[i][j]
			nx.draw_networkx_edges(G,pos,edgelist=[(X[0],X[1])],width=2.5,alpha=0.6,edge_color='r')
			messagebox.showinfo("Edge Selection"," Edge "+str(X[0])+" to "+str(X[1])+" is selected "+"\n\nWeight = "+str(sc)+ "\n\nTotal Cost is " + str(cost))
			plt.pause(1)	
	plt.show()
	return


def CreateGraph():
	G=nx.Graph()
	f=open("kruskalsinput.txt","r")
	n=int(f.readline())
	for i in range(n):
		list1=list(map(int,(f.readline().split())))
		wtmatrix.append(list1)
	for i in range(n):
		for j in range(n)[i:]:
			if wtmatrix[i][j]>0:
				G.add_edge(i,j,length=wtmatrix[i][j])
	return G


def DrawGraph(G):
	pos=nx.spring_layout(G)
	nx.draw(G,pos,with_labels=True)
	edge_label=nx.get_edge_attributes(G,'length')
	nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_label,font_size=11)
	return pos

wtmatrix=[]
if __name__ == "__main__":
	#root = Tk()
	#with open("kruskalsinput.txt", "r") as f:
		#Label(root, text=f.read()).pack()
	#root.mainloop()
	image=Image.open('KRUS.jpg')
	image.show()
	time.sleep(5)	
	G=CreateGraph()
	pos=DrawGraph(G)
	kruskals(G,pos)
	print(pos)
