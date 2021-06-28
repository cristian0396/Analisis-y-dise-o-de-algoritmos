from sys import stdin
import time

def solve(full, est, bol, X, ite, total,pas):
  global ans
  ok = True
  if ite == bol:
  	ans = max(ans, total)
  else:
    tmp = pas.copy()
    j = X[ite][0]

    while j < X[ite][1]:
      cap = X[ite][2] + pas[j] 
      if cap > full:
        ok = False
        j = X[ite][1]
      else:
        pas[j] = pas[j] + X[ite][2]

      j += 1

    if(ok):
      costo = (X[ite][1] - X[ite][0])*X[ite][2]
      solve(full, est, bol, X, ite+1, total+costo,pas)

    pas = tmp
    solve(full, est, bol, X, ite+1, total, pas)

  return ans

def main():
  global ans
  line = list(map(int, stdin.readline().split()))
  while(line != [0,0,0]):
    ans = 0
    X = []
    pas = []
    for i in range(line[2]):
      tcnt = stdin.readline().strip()
      x, y, z = [int(x) for x in tcnt.split()]
      X.append([x,y,z])
    X.sort()
    pas = [0 for _ in range(line[1]+1)]
    print (solve(line[0], line[1], line[2], X, 0,0, pas))
    line = list(map(int, stdin.readline().split()))
main()