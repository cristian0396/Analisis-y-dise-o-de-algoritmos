from sys import stdin

hi = 10000
INF = float('inf')

def phi_tab(X, N, P):
  tab = [INF for i in range(hi+1)]
  tab[0] = 0
  n = 1
  while n != N+1:
  	x = hi - A[n]
  	while x >= 0:
      if tab[x] != INF and tab[x]+1 < tab[x+X[n]]:
	    tab[x+X[n]] = min(tab[x]+1, tab[x+A[n]])
      x -= 1
	n += 1
  x = P

  while tab[x] == INF:
  	x += 1

  return x, tab[X]	

def main():
  tcnt = int(stdin.readline())
  while tcnt!=0:
    total = lo = 0
    valor = int(stdin.readline())
    monedas = int(stdin.readline())
    X = int(stdin.readline()) for i in range(monedas)
    total, lo = phi_tab(X, monedas, valor)
    print('{0} {1}'.format(total, lo))
    tcnt -= 1

main()