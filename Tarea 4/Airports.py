from sys import stdin

class dforest(object):
  """implements an union-find with path-compression and ranking"""

  def __init__(self, size=10):
    """create an empty disjoint forest"""
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 0 for _ in range(size) ]
    self.__csize = [ 0 for _ in range(size) ]
    self.__ccount = self.__size = size

  def __str__(self):
    """return the string representation"""
    return str(self.__parent)

  def __len__(self):
    """return the number of elements in the forest"""
    return self.__size

  def csize(self, x):
    """return the number of elements in the component of x"""
    return self.__csize[self.find(x)]

  def ccount(self):
    """return  the numnber of components"""
    return self.__ccount
  
  def find(self, x):
    """return the representative of the component of x"""
    if self.__parent[x]!=x:
      self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]
  
  def union(self, x, y):
    """perform the union of the collections where x and y belong"""
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      krx,kry = self.__rank[rx],self.__rank[ry]
      if krx>=kry:
        self.__parent[ry] = rx
        self.__csize[rx] += self.__csize[ry]
        if krx==kry: self.__rank[ry] += 1
      else:
        self.__parent[rx] = ry
        self.__csize[ry] += self.__csize[rx]
      self.__ccount -= 1

df = None

def kruskal(G, lenv, A):
  global df
  ans = list()
  G.sort(key = lambda x: x[2])
  df,i = dforest(lenv),0
  for u,v,w in G:
    if df.find(u)!=df.find(v) and w<A:
      ans.append((u, v, w))
      df.union(u, v)
  return ans
    
def main():
  line = int(stdin.readline())
  for i in range(line):
    N,M,A = 
    
    G = list() ; tmp,a = 0,0
    for j in range(M):
      x,y,z = map(int,stdin.readline().split())
      G.append((x-1,y-1,z))

    ans = kruskal(G,N,A)
    for j in range(N):
      if j==df.find(j): 
        a+=1

    for j in range(len(ans)): 
      tmp += ans[j][2]
    tmp += a*A
    print("Case #{0}: {1} {2}".format(i+1,tmp,a))
main()