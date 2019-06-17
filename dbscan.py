import numpy as numpy
import scipy as scipy
from sklearn import cluster
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
import time
from PIL import Image
 
 
image=Image.open('DB.jpg')
image.show()
time.sleep(5) 


def set2List(NumpyArray):
    list = []
    for item in NumpyArray:
        list.append(item.tolist())
    return list
 
 
def GenerateData():
    data = pd.read_csv('xclara.csv')
    print("Input Data and Shape")
    print(data.shape)
    data.head()
    f1 = data['V1'].values
    f2 = data['V2'].values
    X = numpy.array(list(zip(f1, f2)))
    return X
 
 
def DBSCAN(Dataset, Epsilon,MinumumPoints,DistanceMethod = 'euclidean'):
#    Dataset is a mxn matrix, m is number of item and n is the dimension of data
    m,n=Dataset.shape
    Visited=numpy.zeros(m,'int')
    Type=numpy.zeros(m)
#   -1 noise, outlier
#    0 border
#    1 core
    ClustersList=[]
    Cluster=[]
    PointClusterNumber=numpy.zeros(m)
    PointClusterNumberIndex=1
    PointNeighbors=[]
    DistanceMatrix = scipy.spatial.distance.squareform(scipy.spatial.distance.pdist(Dataset, DistanceMethod))
    for i in range(m):
        if Visited[i]==0:
            Visited[i]=1
            PointNeighbors=numpy.where(DistanceMatrix[i]<Epsilon)[0]
            if len(PointNeighbors)<MinumumPoints:
                Type[i]=-1
            else:
                for k in xrange(len(Cluster)):
                    Cluster.pop()
                Cluster.append(i)
                PointClusterNumber[i]=PointClusterNumberIndex
                
                
                PointNeighbors=set2List(PointNeighbors)    
                ExpandClsuter(Dataset[i], PointNeighbors,Cluster,MinumumPoints,Epsilon,Visited,DistanceMatrix,PointClusterNumber,PointClusterNumberIndex  )
                Cluster.append(PointNeighbors[:])
                ClustersList.append(Cluster[:])
                PointClusterNumberIndex=PointClusterNumberIndex+1
                 
                    
    return PointClusterNumber 
 
 
 
def ExpandClsuter(PointToExapnd, PointNeighbors,Cluster,MinumumPoints,Epsilon,Visited,DistanceMatrix,PointClusterNumber,PointClusterNumberIndex  ):
    Neighbors=[]
 
    for i in PointNeighbors:
        if Visited[i]==0:
            Visited[i]=1
            Neighbors=numpy.where(DistanceMatrix[i]<Epsilon)[0]
            if len(Neighbors)>=MinumumPoints:
#                Neighbors merge with PointNeighbors
                for j in Neighbors:
                    try:
                        PointNeighbors.index(j)
                    except ValueError:
                        PointNeighbors.append(j)
                    
        if PointClusterNumber[i]==0:
            Cluster.append(i)
            PointClusterNumber[i]=PointClusterNumberIndex
    return
 
#Generating some data with normal distribution at 
#(0,0)
#(8,8)
#(12,0)
#(15,15)
Data=GenerateData()
 
#Adding some noise with uniform distribution 
#X between [-3,17],
#Y between [-3,17]
noise=scipy.rand(50,2)*20 -3
 
Noisy_Data=numpy.concatenate((Data,noise))
size=20
 
 
fig = plt.figure()
ax1=fig.add_subplot(2,1,1) #row, column, figure number
ax2 = fig.add_subplot(212)
 
ax1.scatter(Data[:,0],Data[:,1], alpha =  0.5 )
plt.pause(1)
ax1.scatter(noise[:,0],noise[:,1],color='red' ,alpha =  0.5)
plt.pause(1)
ax2.scatter(noise[:,0],noise[:,1],color='red' ,alpha =  0.5)
 
 
Epsilon=1
MinumumPoints=20
result =DBSCAN(Data,Epsilon,MinumumPoints)
 
#printed numbers are cluster numbers
print(result)
#print "Noisy_Data"
#print Noisy_Data.shape
#print Noisy_Data
 
for i in range(len(result)):
	plt.pause(0.0000000000000000000000001)
	ax2.scatter(Noisy_Data[i][0],Noisy_Data[i][1],color='yellow' ,alpha =  0.5)
      
plt.show()