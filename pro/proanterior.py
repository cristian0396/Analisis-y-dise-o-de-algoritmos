from sys import stdin

def solve(mi,A):
	bi = list(mi)
	for i in A:
		if bi[i[0]] == 0:
			j = i[0]
			while j>0:
				if bi[j] == 1:
					i[0] = j
					j = 0
				j -= 1
		if bi[i[1]] == 0:
			j = i[1]
			while j<len(bi):
				if bi[j] == 1:
					i[1] = j
					j = len(bi)
				j += 1

		ite = i[1]-i[0]
		for j in range(ite+1):
			if bi[i[0]+j] == "1":
				bi[i[0]+j] = "0"
			else: 
				bi[i[0]+j] = "1"
			print("Cambio:", bi)
			
	ans = ''.join(bi)
	print("holi", ans)
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
		print ("este es el bi", bi)
		ans = solve(bi, A)
		ans = hex(int(ans,2))[2:]
		print(ans)	
		tcnt -= 1
main()

64E0 = 000110010011100000

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
0 0 0 1 1 0 0 1 0 0  1  1  1  0  0  0  0  0

5, 12
0 0 0 1 *0 1 1 0 1 1  0  0*  1  0  0  0  0  0

10, 11
0 0 0 1 0 1 1 0 1 *0  1  1  0*  0  0  0  0  0

5, 8
0 0 0 *0 1 0 0 1 0* 0  1  1  0  0  0  0  0  0

3, 6
0 0 *1 1 0 1 1 0* 0 0  1  1  0  0  0  0  0  0

1, 17
*1 1 0 0 1 0 0 1 1 1  0  0  1  1  1  1  1*  0 = 3273E



1
3 6
0 = 000

1 2
*1 1* 0
1 3
*0 0 1*
1 3
*1 1 0*
2 3
1 *0 1*
1 3
*0 1 0*
1 3
*1 0 1*


7 13
    7 6 5 4 3 2 1 
E = 0 0 0 1 1 1 0
    
7-1+1, 7-3+1
7 5
	1 1 1 0 1 1 | 0|
		  
7-7+1 7-7+1
1 1
1 1 1 0 1 *0 1*

3 7
1 1*0 1 0 1 0*

2 6
1*0 1 0 1 0*0
5 5
1 0 1 0*0*0 0
5 7
1 0 *0 1 1 1 1*
2 5
*0 1 1 0 0* 1 1
1 1
*1 0*1 0 0 1 1
3 5
1 0 *0 1 1 0* 1
1 2
*0 1 1 0* 1 0 1
1 3
*1 0 0*0 1 0 1 
5 6
1 0 0 0 *0 1 0*
2 4
*0 1 1 1 1 0* 0
3C







9 4

67 = 001100111
 1 2 3 4 5 6 7 8 9 
 0 0 1 1 0 0 1 1 1

1 2
*1 1 0*1 0 0 1 1 1

2 4
 1*0 1 0*0 0 1 1 1

2 7
*0 1 0 1 1 1 0*1 1

6 8
 0 1 0 1 1*0 1 0*1
B5 = 10110101