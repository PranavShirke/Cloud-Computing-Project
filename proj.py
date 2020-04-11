import networkx.algorithms.approximation
import networkx as nx
import numpy as np
f = open("as19971108.txt","r")
G = nx.Graph()
i =  0
for line in f:
    i = i+1
    if i > 4:
        line = line.replace("\n","")
        t = line.split("\t")
        if t[0] != t[1]:
            x = (np.random.rand()%10)/10
            G.add_edge(t[0],t[1],weight = x)
print(len(nx.minimum_edge_cut(G)))
# T = nx.algorithms.approximation.steinertree.metric_closure(G)
# print(nx.Graph.size(T))
