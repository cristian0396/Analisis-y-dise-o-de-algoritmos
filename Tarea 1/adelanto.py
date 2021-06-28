"""def binSearch(k):
	"""
	Retorna el indice de la sumatoria 
	"""
	ans = -1
	n = 0
	low, hi = 0, 65000
	while (low+1 != hi):
		mid = (low+hi)>>1
		if((mid*(mid+1)>>1)>k):
			ans = hi
			mid = hi
		else:
			low += 1

	if mid*(mid+1)>>1== k:
    ans=mid*(mid+1)>>1
  else:
    while((n*(n+1)>>1)-k != 0):
      n += 1

	return n"""

def solve(k):
  ans = -1
  n = 0
  low, hi = 0, 65000
  while (low+1 != hi):
    mid = (low+hi)>>1
    if((mid*(mid+1)>>1)>k):
      ans = hi
      mid = hi
    else:
      low += 1

  if mid*(mid+1)>>1== k:
    ans=mid*(mid+1)>>1
  else:
    while((n*(n+1)>>1)-k != 0):
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

main()