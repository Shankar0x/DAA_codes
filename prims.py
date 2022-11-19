import sys
class graphs():
    def __init__(self,verts):
        self.v=verts
        self.graph=[[0 for cols in range(verts) for row in range(verts)]]

    # secondly 
    def minkey(self,key,mstset):
        mini=sys.maxsize
        for i in range(self.v):
            if key[i]<mini and mstset[i]==False:
                mini=key[i]
                mini_ind=i
        return mini_ind
    # Lastly
    def printMST(self,parent):
        print("Edge\tWeight")
        for i in range(1,self.v):
            print(parent[i],'-',i,'\t',self.graph[i][parent[i]])
    # firstly
    def primMST(self):
        # generate 3 lists
        # 1. keys of all infinity first 0
        # 2. mstset of all False boolean
        # 3. parent of all 0 first -1
        keys=[sys.maxsize]*self.v
        mstset=[False]*self.v
        parent=[0]*self.v

        keys[0]=0
        parent[0]=-1

        for _ in range(self.v):
            # pick the minimum weight from keys
            # make mstset True for it
            # update its own and adjacent verts' parents 
            i = self.minkey(keys,mstset)
            mstset[i]=True

            for j in range(self.v):
                # if connection present AND not inclued
                # already AND already present weight HIGHER than value relaxed now
                if self.graph[i][j]>0 and mstset[j]==False and keys[j]>self.graph[i][j]:
                    keys[j]=self.graph[i][j]
                    parent[j]=i
        self.printMST(parent)

g = graphs(5)
g.graph = [[0, 2, 0, 6, 0],
			[2, 0, 3, 8, 5],
			[0, 3, 0, 0, 7],
			[6, 8, 0, 0, 9],
			[0, 5, 7, 9, 0]]
g.primMST()