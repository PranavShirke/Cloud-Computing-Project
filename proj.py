import networkx as nx

f = open("as19971108.txt","r")
G = nx.Graph()
i =  0
for line in f:
    i = i+1
    if i > 4:
        line = line.replace("\n","")
        t = line.split("\t")
        G.add_edge(t[0],t[1])