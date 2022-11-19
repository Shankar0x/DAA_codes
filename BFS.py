'''
Reference materials
1. https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/
2. https://www.geeksforgeeks.org/defaultdict-in-python/
'''

from collections import defaultdict
class graph:
    def __init__(self):
        self.g=defaultdict(list)
    def addEdge(self,u,v):
        self.g[u].append(v)
    def BFS(self,s):
        visited=[False]*len(self.g)
        queue=[]
        queue.append(s)
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            visited[s]=True
            for i in self.g[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)