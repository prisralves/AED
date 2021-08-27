##################################
#PROJETO FINAL
# Data: 11/08/2021
##################################

"""
NETWORK SURVIVABILITY (qual a probabilidade de sobrevivência da rede, força bruta, sobrevive a qualquer ataque, falhas individuais, isoladas, gargalos, ponto frágil)
INSTANCE: Graph G = (V, E), a rational "failure probability" p(x), 0 ≤ p(x) ≤ 1, for each x ϵ V υ E, a positive rational number q ≤ 1.
QUESTION: Assuming all edge and vertex failures are independent of one another, is the probability q or greater that for all {u, v} ϵ E at least one of u,v ou {u, v} will fail?

"""
#########################
# Imports
#########################
# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

#########################
# Classes e funções
#########################
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 


#########################
# Programa Principal
#########################
# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)