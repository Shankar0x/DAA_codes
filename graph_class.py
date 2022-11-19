class worder:
  def __init__(self,word_grid,dict1):
    self.word_grid=word_grid
    self.dict1=dict1
    self.found_set=[]
    self.found_path=[]
  def dfs_grid(self,stri,j,k,m,n,i,path):
    if j>=m or k>=n or stri[i] != self.word_grid[j][k] or j<0 or k<0:
      return False
    path.append((j,k))
    if i == len(stri)-1:
      return True
    foc=self.word_grid[j][k]
    self.word_grid[j][k]='visited'

    col1=bool(self.dfs_grid(stri,j,k+1,m,n,i+1,path)) or bool(self.dfs_grid(stri,j,k-1,m,n,i+1,path)) or bool(self.dfs_grid(stri,j+1,k,m,n,i+1,path))
    col2=bool(self.dfs_grid(stri,j-1,k,m,n,i+1,path)) or bool(self.dfs_grid(stri,j+1,k+1,m,n,i+1,path))
    col3=bool(self.dfs_grid(stri,j-1,k+1,m,n,i+1,path)) or bool(self.dfs_grid(stri,j+1,k-1,m,n,i+1,path)) or bool(self.dfs_grid(stri,j-1,k-1,m,n,i+1,path))

    self.word_grid[j][k]=foc

    return bool(col1 or col2 or col3)
      
  def gridfinder(self):
    m=len(self.word_grid)
    n=len(self.word_grid[0])
    path=[]
    for i in range(len(self.dict1)):
      stri=self.dict1[i]
      
      for j in range(m):
        for k in range(n):
          if(self.dfs_grid(stri,j,k,m,n,0,path)):
            self.found_set.append(stri)
            self.found_path.append(path)
            calc_score=2*len(stri)
            print('------------------------\nWord: '+stri+'\nScore: '+str(calc_score)+'\nPath: '+str(path))
            path=[]
  def wordfinder(self,s):
    lis=[]
    for i in self.found_set:
      if i.startswith(s):
        lis.append(i)
    print("All the words that were found which starts with \'"+s+"\' are: ",lis)

"""##**Output**"""

if __name__ == '__main__':
  word_grid=[
      ['e','f','r','a'],
      ['h','g','d','r'],
      ['p','s','n','a'],
      ['e','e','b','e']
  ]
  dict1 =  ['an', 'and', 'bad', 'badge','ban', 'band', 'bane', 'bang',
    'bangs', 'bans', 'be', 'bean', 'beans', 'bear', 'beard', 'beards',
    'bee', 'been', 'beep', 'beeps', 'bees', 'dab', 'dabs', 'dane',
    'danes', 'darn', 'drab', 'ear', 'earn', 'earns', 'end', 'ends',
    'grad', 'grads', 'he', 'pen', 'pend', 'pens', 'ran', 'rang', 'range', 'see', 'seen', 'seep', 'she' ]

  wordObj=worder(word_grid,dict1)
  wordObj.gridfinder()
  wordObj.wordfinder('a')
  wordObj.wordfinder('s')