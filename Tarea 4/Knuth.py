from sys import stdin
from collections import deque


def phi(arr):
  A = deque()
  A.append([])
  B = deque()
  C = [A, B]

  tmp = 0
  while(arr):
  	permu(C[tmp], C[not tmp], arr.pop())
  	tmp = not tmp

  while(C[tmp]):
  	ans = C[tmp].popleft()
  	print("".join(i for i in ans))


def permu(A, B, ult):
  while(A):
    D = A.popleft()
    for i in range(len(D)+1):
      tmp = D[:]
      tmp.insert(i, ult)
      B.append(tmp)

  return B

def main():
  tcnt = stdin.readline().strip()
  while (len(tcnt) != 0):
  	ans = list(tcnt)
  	ans.reverse()
  	phi(ans)
  	tcnt = stdin.readline().strip()
  	if tcnt != "": print()

main()
