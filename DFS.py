from collections import defaultdict
class graph:
    def __init__(self):
        self.g=defaultdict(list)
    def addEdge(self,u,v):
        self.g[u].append(v)
    def DFSutil(self,visited,v):
        visited.add(v)
        print(v,end=" ")
        for n in self.g[v]:
            if n not in visited:
                self.DFSutil(visited,n)

    def DFS(self,v):
        visited=set()
        self.DFSutil(visited,v)

if __name__ == "__main__":
	g = graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is DFS from (starting from vertex 2)")
	# Function call
	g.DFS(2)
    