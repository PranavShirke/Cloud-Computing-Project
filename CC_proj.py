import networkx as nx
import random
import numpy as np
G =nx.Graph()
S = nx.Graph()
def main():


		with open("test.txt","r") as fp:
			line = fp.readline()
	 		
			while line:
				line = line.replace("\n","")
				a=line.split("\t")
				line = fp.readline()
				x = (np.random.rand()%10)/10
				G.add_edge(a[0],a[1],weight=x)
		
		sum=0
		mdegree =0
		for j in list(G.nodes()):
			sum+=G.degree(j)
			if G.degree(j)>mdegree:
				mdegree=G.degree(j)
													#Degree of a node 
		avgdegree= sum/len(list(G.nodes()))
		print(avgdegree)							#avg degree
		print(mdegree)								#max degree

		print(G.size(weight='weight'))					#Total cost of network

		
	
 
if __name__ == '__main__':
    main()
