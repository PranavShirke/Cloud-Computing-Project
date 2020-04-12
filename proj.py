import networkx.algorithms.approximation
import networkx as nx
import numpy as np


def add_new_node(G):

    t = list(G.nodes())
    for item in t:
        item = int(item)
    maxi = int(max(t))
    maxi += 1
    td = np.random.randint(0, len(t))
    G.add_edge(str(maxi), t[td])
    return G


def mutation(G):
    t = list(G.nodes())
    td1 = np.random.randint(0, len(t))
    td2 = np.random.randint(0, len(t))
    l1 = list(G.edges(t[td1]))
    l2 = list(G.edges(t[td2]))
    for item in l1:
        G.remove_edge(item[0],item[1])
        G.add_edge(t[td2],item[1])
    for item in l2:
        G.remove_edge(item[0],item[1])
        G.add_edge(t[td1],item[1])



def min_cut_edge(G):
    return len(nx.minimum_edge_cut(G))


def time_delay(G):
    T = nx.algorithms.approximation.steinertree.metric_closure(G)
    return nx.Graph.size(T)





f = open("as19971108.txt","r")
G = nx.Graph()
i =  0
for line in f:
    i = i+1
    if i > 4:
        line = line.replace("\n","")
        t = line.split("\t")
        if t[0] != t[1]:
            # x = (np.random.rand()%10)/10
            G.add_edge(t[0],t[1],weight = 1)
mutation(G)







