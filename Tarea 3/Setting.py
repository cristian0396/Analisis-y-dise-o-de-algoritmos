from sys import stdin

def phi(S, G):
	global col
	sumaS = 0
	sumaG = 0
	for i in range(len(S)):
		sumaS = sumaS + S[i]

	sumaS = sumaS + G[col-1]

	for i in range(len(G)):
		sumaG = sumaG + G[i]
		
	sumaG = sumaG + S[0]

	suma=max(sumaS, sumaG)

	return suma

def main():
	global col
	tcnt = stdin.readline().strip()
	while tcnt != "":
		col = int(tcnt)
		S = list(map(int, stdin.readline().split()))
		G = list(map(int, stdin.readline().split()))
		S.sort()
		G.sort()
		G.reverse()
		print(phi(S,G))
		tcnt = stdin.readline().strip()
main()