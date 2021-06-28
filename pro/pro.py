"""
Christian Roman
8922142
"""
from sys import stdin

def solve(mi,A):
	bi = list(mi)
	for i in A:
		low = i[0]-1
		top = i[1]-1
		if bi[low] == "0":
			j = low
			while j>=0:
				if bi[j] == "1":
					low = j
					j = 0
				j -= 1
		if bi[top] == "0":
			j = top
			while j < len(bi):
				if bi[j] == "1":
					top = j
					j = len(bi)
				j += 1
		ite = top-low
		j = 0
		while j< ite+1:
			if bi[low+j] == "1":
				bi[low+j] = "0"
			else: 
				bi[low+j] = "1"
			j += 1
	ans = ''.join(bi)
	return ans

def main():
	conts = 16
	tcnt = int(stdin.readline())
	while(tcnt > 0):
		K, M = map(int, stdin.readline().split())
		ex = stdin.readline()
		bi = str(bin(int(ex, conts))[2:].zfill(K))
		i = 0
		A = list()
		while i < M:
			ini, fin = map(int, stdin.readline().split())
			A.append((ini,fin))	
			i += 1
		ans = solve(bi, A)
		ans1 = hex(int(ans,2))[2:].upper()
		print(ans1)	
		tcnt -= 1
main()