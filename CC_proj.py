import networkx as nx
import random
import numpy as np
G1 =nx.Graph()
G2 = nx.Graph()
G3 = nx.Graph()
G4 = nx.Graph()
def main():


		with open("test.txt","r") as fp:
			line = fp.readline()
	 		
			while line:
				line = line.replace("\n","")
				a=line.split("\t")
				line = fp.readline()
				x = (np.random.rand()%10)/10
				y = (np.random.rand()%9)/10
				G1.add_edge(a[0],a[1],weight=x)
				G2.add_edge(a[0],a[1],weight=x)

		
		sum1=0
		mdegree1 =0
		sum2=0
		mdegree2=0
		for j in list(G1.nodes()):
			sum1+=G1.degree(j)
			if G1.degree(j)>mdegree1:
				mdegree1=G1.degree(j)
		for j in list(G2.nodes()):
			sum2+=G2.degree(j)
			if G2.degree(j)>mdegree2:
				mdegree2=G2.degree(j)
													#Degree of a node 
		avgdegree1= sum1/len(list(G1.nodes()))

		#print(avgdegree1)							#avg degree
		#print(mdegree1)								#max degree

		print(G1.size(weight='weight'))					#Total cost of network
		print(G2.size(weight='weight'))
		def crossover (G1,G2):

				t1 = list(G1.edges())
				t2 = list(G2.edges())
				x = random.randint(0,len(t1))
				for j in range(x):
					#print(G1.get_edge_data(*t1[j])['weight'])
					G3.add_edge(*t1[j],weight = G1.get_edge_data(*t1[j])['weight'])	

				z = x
				#print(x)
				for k in range(len(t2)):
						if z == len(t1):
							break
						else:
							if t2[k] not in t1 : 
								G3.add_edge(*t2[k], weight = G1.get_edge_data(*t2[k])['weight'])
						z=z+1

				z = x

				for j in range(len(t1)-x):
					G4.add_edge(*t1[j],weight = G1.get_edge_data(*t1[j])['weight'])

				for k in range(len(t2)-x):
						if z == len(t1):
							break
						else:
							if t2[k] not in t1 : 
								G4.add_edge(*t2[k], weight = G1.get_edge_data(*t2[k])['weight'])
						z=z+1

		crossover(G1,G2)			
		print(G3.size(weight='weight'))
		print(G4.size(weight='weight'))
		
	
 
if __name__ == '__main__':
    main()
