class graph:
    def __init__(self,vertices):
        self.v=vertices
        self.g=[]
    def addedge(self,u,v,w):
        self.g.append([u,v,w])
        # adding edge list with src dest wei format
    def find(self,parent,i):
        if parent[i]==i:
            return i
            # root case
        return self.find(parent,parent[i])
    def union(self,parent,rank,x,y):
        xroot=