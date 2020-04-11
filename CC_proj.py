import networkx as nx
G =nx.Graph()
def main():


		with open("test.txt","r") as fp:
			line = fp.readline()
	  
			while line:
				a=line.split()
				line = fp.readline()
				G.add_edge(a[0],a[1])
		T=nx.minimum_spanning_tree(G)
if __name__ == '__main__':
    main()
