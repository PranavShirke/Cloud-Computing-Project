import networkx as nx

f = open("as19971108.txt","r")
G = nx.Graph()
i =  0
for line in f:
    i = i+1
    if i > 4:
        line = line.replace("\n","")
        t = line.split("\t")
        if t[0] != t[1]:
            G.add_edge(t[0],t[1],weight = 0)
T = nx.minimum_spanning_tree(G)
for j in list(G.edges()):
    print(nx.shortest_path(T, source = j[0], target = j[1]))
