"""
Colaborador: Sebastian Toro
"""
def solve(N,L,U):
	i,M = 31,0 
	while(i >= 0):
		mask = M|(1<<i)
		if( (((N>>i)&1) == 0 and mask <= U) or mask<=L ):
			M=mask
		i-=1 
	return M
from sys import stdin

def phi(N,L,U):

	i,M = 31,0 
	while(i >= 0):
		mask = M|(1<<i)
		if( (((N>>i)&1) == 0) or mask<=L ):
			if(mask <= U):
				M=mask
		i-=1

	return M

def main():
	line=stdin.readline().strip()
	while line != "":
		N, L, U = list(map(int, line.split()))
		M = phi(N,L,U)
		print(M)
		line=stdin.readline().strip()

main()