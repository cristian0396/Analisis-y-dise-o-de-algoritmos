from sys import stdin

num = []

def phi(n, NUM, curr):
  if n == N-1:
    return((curr>>1)&1) == ((first>>2)&1) and (Curr&1) == ((first>>1)&1)

  visited[n][curr] = True
  for i in range(NUM):
    if (((id>>i)&1) == num[n+1]-'0' and ((curr>>1)&1) == ((i>>2)&1) and (curr&1) == ((i>>1)&1)):
  	  if (n < N-1 and not(visited[n+1][i]) and phi(n+1, i)):
  	  	return True
  return False	

def main():
  tcnt = list(map(int,stdin.readline().split()))
  while tcnt != "":
    id = tcnt[0]
    N = tcnt[1]
    state = tcnt[2]
    found = False
    for i in range(8):
      if found and (((id>>i)&1) == state[0]-'0'):
        for j in range(N):
      	  memset(visited[j], False, states)
        first = i
        found = phi(0,tcnt[1],i)
    if not(found):
      print("GARDEN OF EDEN")
    else:
      print("REACHABLE")
    tcnt = list(map(int,stdin.readline().split()))
main()