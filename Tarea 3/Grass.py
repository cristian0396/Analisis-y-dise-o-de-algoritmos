"""
colaboradores: codigo del bitbucket de camilo rocha y Nicolas Alvarez
https://bitbucket.org/snippets/hquilo/z6KbA
"""
from sys import stdin
from math import * 

def phi(L,H,a):
  a.sort()
  ans,low,n,ok,N = list(),L,0,True,len(a)
  while ok and low<H and n!=N:
    ok = a[n][0]<=low
    best,n = n,n+1
    while ok and n!=N and a[n][0]<=low:
      if a[n][1]>a[best][1]:
        best = n
      n += 1
    ans.append(best)
    low = a[best][1]
  ok = ok and low>=H
  if ok==False:
    ans = list()
  return ans

def main():
  line= stdin.readline().strip()
  while line != "":
    arr=[]
    L, H, a = list(map(int, line.split()))
    for i in range(0,L):
      pos, R = map(int, stdin.readline().strip().split())
      if R*2>a:
        dis= sqrt((R**2) - ((a/2)**2))
        arr.append([pos-dis,pos+dis])
    arr.sort()
    ans = phi(0,H,arr)

    if len(ans)==0:
      print(-1)
    else:
      print(len(ans))
    line = stdin.readline().strip()

main()