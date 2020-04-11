import networkx as nx
import random
G =nx.Graph()
S = nx.Graph()
def main():


		with open("test.txt","r") as fp:
			line = fp.readline()
	 		
			while line:
				a=line.split()
				line = fp.readline()
				G.add_edge(a[0],a[1])
		

		print(len(nx.minimum_edge_cut(G)))

	
 
if __name__ == '__main__':
    main()
