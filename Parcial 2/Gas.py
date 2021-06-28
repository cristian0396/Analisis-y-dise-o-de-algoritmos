from sys import stdin

def solve(l, g, x):
  ans = 0
  gas = list()
  i = 0
  low = 0
  ok = True
  while i != len(x) and low < l and ok:
    ok = x[i][0] <= low
    best, i = i, i+1
    while i != len(x) and x[i][0] <= low and ok:
      if x[i][1] > x[best][1]:
        best = i
      i += 1
    low = x[best][1]
    gas.append(best)

  ok = ok and low >=l

  if ok == False:
  	gas = list()

  if (len(gas) == 0):
    ans = -1
  else:
  	ans = g - len(gas)

  return ans

def main():
  line = list(map(int, stdin.readline().split()))
  while(line[1] != 0 and line[0] != 0):
  	X = list()
  	for i in range(line[1]):
  	  tcnt = stdin.readline().strip()
  	  xi, ri = [int(x) for x in tcnt.split()]
  	  X.append([xi-ri, xi+ri])
  	X.sort()
  	print (solve(line[0], line[1], X))
  	line = list(map(int, stdin.readline().split()))

main()