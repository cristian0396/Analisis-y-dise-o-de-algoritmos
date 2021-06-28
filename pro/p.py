"""Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
Christian Roman - 8922142"""
from sys import stdin

"""Entrada: dos parametros que son el numero entero (bi) que se maneja como un binario y el entero (bot) que es limite inferior.
Retorna la posicion bot más las x posiciones en las que se encuentra el primer uno"""
def izq(bi, bot):
	"""Esta función busca el primer uno (1) que se encuentre en direccion izquierda, opteniendo la parte izquierda donde 
	se buscara el uno mas cercano y contará las posiciones para sumarlas al limite inferior (bot)"""
	num = (bi>>bot)
	x = (num&-num).bit_length()
	return bot+x

"""Entrada: dos parametros que son el numero entero (bi) que se maneja como un binario y el entero (top) que es limite supeior.
Retorna la posicion ans que es el tamaño de la cadena del uno mas significativo para actualizar el limite superior (top)"""
def der(bi, top):
	"""Esta función busca el primer uno (1) que se encuentre en direccion derecha, haciendo un and con la parte derecha
	que es la que necesito, para encontrar el primer uno hacia la derecha"""
	num = bi & (1<<top-1)-1
	ans = num.bit_length()
	if ans == 0: ans=top
	return ans

"""Entrada: dos parametros un numero entero (bi) que se maneja como un binario y una lista de tuplas (A) donde se encuentran 
almacenados los limites superiores e inferiores. Retorna el numero entero despues de aplicarle el cambio en los limites obtenidos"""
def solve(bi, A):
	"""Esta funcion verifica los limites superior e inferior, si estan prendidos (1) simplemente hace un XOR para cambiar 
	la cadena binaria justo en los limites verificados, en caso de que esten apagados (0) entrará en los condicionales
	y actualizará los limites para poder hacer el cambio respectivo"""
	for i in A:
		bot, top = map(int, i)
		if bi & (1<<bot-1) == 0: bot = izq(bi, bot)
		if bi & (1<<top-1) == 0:top = der(bi, top)
		bi = bi^((1<<bot-top+1)-1)<<top-1
	return bi

def main():
	global K
	tcnt = int(stdin.readline())
	while(tcnt > 0):
		K, M = map(int, stdin.readline().split())
		ex = stdin.readline()
		bi = int(ex, 16)
		i = 0
		A = list()
		while i < M:
			ini, fin = map(int, stdin.readline().split())
			A.append((K-ini+1,K-fin+1))	
			i += 1
		print (hex(solve(bi,A))[2:].upper())
		tcnt -= 1
main()

