"""
Colaboradores: curso pasado UVa 10986 solución por Camilo Rocha
https://drive.google.com/file/d/1ZrK0CtylM6xbSH-BwwxMYM3ED56Agq0O/view
"""

from sys import stdin
from heapq import heappush, heappop

INF = float('inf')

def solve(A, E):
  visited = [False for _ in A]
  dist = [INF for _ in A] 
  queue, dist[E] = [(0,E)], 0

  while len(queue) != 0:
    d, u =heappop(queue)
    if visited[u] == False:
      visited[u] = True
      for v,w in A[u]:
        duv = d + w
        if dist[v]>duv:
          dist[v] = duv
          heappush(queue, (duv, v))

  return dist

def main():
  tcnt = int(stdin.readline())
  while tcnt != 0:
    stdin.readline()
    N = int(stdin.readline())
    E = int(stdin.readline())-1
    T = int(stdin.readline())
    M = int(stdin.readline())
    A = [list() for _ in range(N)]

    for i in range(M):
      a, b, d = map(int, stdin.readline().split())
      A[b-1].append((a-1, d))
    ANS = solve(A, E)
    ans = 0
    for i in ANS:
      if i <= T:
        ans += 1

    print(ans)
    print()
    tcnt -= 1

main()