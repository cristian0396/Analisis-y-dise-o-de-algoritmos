from sys import stdin

def solve(k):
  ans = -1
  n = 0
  low, hi = 0, len[k]
  while (low+1 != hi):
    mid = (low+hi)>>1
    if((mid*(mid+1)>>1)>k):
      ans = hi
      hi = mid
    else:
      low = mid

  n = ans
  
  if k == 0:
    n = 3
    
  while(((n*(n+1)>>1)-k) % 2 != 0):
    n += 1
    
  return n

def main():
  tcnt,first = int(stdin.readline()),True
  while tcnt!=0:
    stdin.readline()
    if first==False: print()
    first = False
    print(solve(int(stdin.readline())))
    tcnt -= 1

solve(1000000000)
