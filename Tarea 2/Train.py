from sys import stdin
"""
Basado en el codigo LS de Rocha hecho en clase

"""

def ls (A, lena):
  ans = 0
  A.reverse()
  lis,lds = [ None for _ in range(lena) ],[ None for _ in range(lena)]
  for n in range(lena):
    lis[n] = lds[n] = 1
    for i in range(n):
      if A[i] <= A[n] and lis[i] >= lis[n]: lis[n] = lis[i] + 1
      if A[i] >= A[n] and lds[i] >= lds[n]: lds[n] = lds[i] + 1
    ans = max(lis[n]+lds[n]-1, ans)
  return ans

def main():
  tcnt = int(stdin.readline())
  while tcnt!=0:
    text = int(stdin.readline())
    arr = []
    i = 0
    if text == 0:
      print(0)
    else:
      while i<text:
        new = int(stdin.readline())
        arr.append(new)
        i += 1
      print(ls(arr,text))
    tcnt -= 1

main()
