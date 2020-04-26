import networkx.algorithms.approximation
import networkx as nx
import numpy as np
from numpy import random



def crossover (G1,G2):

    Gc1 = nx.Graph()
    Gc2 = nx.Graph()
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
    return Gc1, Gc2



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
        x = np.random.randint(0, 2)
        if x % 2 == 0:
            w =  G.get_edge_data(item[0], item[1])['weight']
            G.remove_edge(item[0],item[1])
            G.add_edge(t[td2],item[1], weight = w)
    for item in l2:
        x = np.random.randint(0, 2)
        if x % 2 == 0:
            w =  G.get_edge_data(item[0], item[1])['weight']
            G.remove_edge(item[0],item[1])
            G.add_edge(t[td1],item[1], weight = w)
    return G


def min_cut_edge(G):
    return len(nx.minimum_edge_cut(G))


def time_delay(G):
    T = nx.algorithms.approximation.steinertree.metric_closure(G)
    return nx.Graph.size(T)


def fitness(x):
    return 2

mutation_rate = 5
n = 9 #number of genes
niter = 10
child_option = 1 #whether to mutate children if disconnected or wether to simply drop them
genes = []
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

#generate initial population

genes.append(G)
t = mutation(G)
for i in range(n):
    while(nx.is_connected(t)==False):
        t = mutation(t)
        # print('here1')
    genes.append(t)
    # print('here2')
n = n+1
# genes = [1,2,3,4,5,6,7,7,8,10]
score = []
for i in range(n):
    score.append(fitness(genes[i]))

for q in range(niter):
    children = []
    children_score = []
    # score = score/np.sum(score)
    for i in range(int(n/2)):
        x = np.random.choice(n, 2, p=score/np.sum(score))
        a, b = crossover(genes[x[0]],genes[x[1]])
        if child_option == 0:
            while(nx.is_connected(a)==False):
                a = mutation(a)
                print('here1')
            while(nx.is_connected(b)==False):
                b = mutation(b)
                print('here2')
            children.append(a)
            children.append(b)
            children_score.append(fitness(a))
            children_score.append(fitness(b))
        else:
            if nx.is_connected(a)==True:
                children.append(a)
                children_score.append(fitness(a))
            if nx.is_connected(b)==True:
                children.append(b)
                children_score.append(fitness(b))
        
    # genes = list(genes)
    score = list(score)
    genes.extend(children)
    score.extend(children_score)
    genes = [x for _,x in sorted(zip(score,genes), key = lambda x: x[0], reverse = True)][:n]
    score = sorted(score, reverse = True)[:n]
    for i in range(n):
        x = np.random.choice(100)
        if x < mutation_rate:
            genes[i] = mutation(G)
            score[i] = fitness(genes[i])
    print('here')
print(score)
print(genes)






