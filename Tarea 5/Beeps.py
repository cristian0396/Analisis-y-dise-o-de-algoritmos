from sys import stdin
import math
INF = float('inf')

def tsp_dp(v, A, vs, n, memo, adj):
  ans = INF
  if (v,A) in memo:
    ans = memo[(v,A)]
  else:
    if A == (1<<n) - 1:
      ans = adj[v][vs]
    else:
      for i in range(n):
        if i != v and (A & (1<<i)) == 0:
          ans = min(ans, adj[v][i] + tsp_dp(i, (A | (1<<i)), vs,n,memo,adj))
    memo[(v,A)] = ans
  return ans

def main():
	tcnt = int(stdin.readline().strip())
	while tcnt > 0:
		tam = stdin.readline()
		x, y = map(int, stdin.readline().strip().split())
		num = int(stdin.readline())
		A = []
		memo = [[ 0 for _ in range(num+1)] for _ in range(num+1)]
		for i in range(num):
			xi, yi = map(int, stdin.readline().strip().split())
			A.append([xi,yi])
		A.append([x,y])
		for i in range(num+1):
			for j in range(num+1):
				memo[i][j] = abs(A[i][0]-A[j][0])+abs(A[i][1]-A[j][1])
		dic = {}
		#ans = tsp_dp(0,0,0,num+1,dic,memo)
		for i in range(len(A)):
			print(memo[i])
		print("The shortest path has length", ans)
		tcnt -= 1
main()