import networkx as nx
import random
import numpy as np
G1 =nx.Graph()
G2 = nx.Graph()
G3 = nx.Graph()
G4 = nx.Graph()
G5 =nx.Graph()
G6 = nx.Graph()
G7 = nx.Graph()
G8 = nx.Graph()
G9 = nx.Graph()
G10 = nx.Graph()
Gc1 = nx.Graph()
Gc2 = nx.Graph()

def main():


		with open("test.txt","r") as fp:
			line = fp.readline()
	 		
			while line:
				line = line.replace("\n","")
				a=line.split("\t")
				line = fp.readline()
				x = (np.random.rand()%10)/10
				y = (np.random.rand()%9)/10
				a1 = (np.random.rand()%8)/10
				b1 = (np.random.rand()%7)/10
				c1 = (np.random.rand()%6)/10
				d1 = (np.random.rand()%5)/10
				e1 = (np.random.rand()%4)/10
				f1 = (np.random.rand()%3)/10
				g1 = (np.random.rand()%2)/10
				h1 = (np.random.rand()%11)/10
				G1.add_edge(a[0],a[1],weight=x)
				G2.add_edge(a[0],a[1],weight=y)
				G3.add_edge(a[0],a[1],weight=a1)
				G4.add_edge(a[0],a[1],weight=b1)
				G5.add_edge(a[0],a[1],weight=c1)
				G6.add_edge(a[0],a[1],weight=d1)
				G7.add_edge(a[0],a[1],weight=e1)
				G8.add_edge(a[0],a[1],weight=f1)
				G9.add_edge(a[0],a[1],weight=g1)
				G10.add_edge(a[0],a[1],weight=h1)

				

		l = [G1,G2,G3,G4,G5,G6,G7,G8,G9,G10]
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
					Gc1.add_edge(*t1[j],weight = G1.get_edge_data(*t1[j])['weight'])	

				z = x
				#print(x)
				for k in range(len(t2)-1,x,-1):
						if z == len(t1):
							break
						else:
							if t2[k] not in t1 : 
								Gc1.add_edge(*t2[k], weight = G1.get_edge_data(*t2[k])['weight'])
						z=z+1

				x = random.randint(0,len(t2))
				for j in range(x):
					Gc2.add_edge(*t2[j],weight = G1.get_edge_data(*t2[j])['weight'])

				z=x

				for k in range(len(t1)-1,x,-1):
						if z == len(t1):
							break
						else:
							if t1[k] not in t2 : 
								Gc2.add_edge(*t1[k], weight = G1.get_edge_data(*t1[k])['weight'])
						z=z+1

		#for i in range()
		for i in range(0,len(l),2):
			crossover(l[i],l[i+1])	
			print(i)		
			print(Gc1.size(weight='weight'))
			print(Gc2.size(weight='weight'))
		
	
 
if __name__ == '__main__':
    main()
