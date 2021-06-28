from sys import stdin

def phi(S):
    s1 = S + 1 
    s2 = S - 1
    cont = 0
    if (S == 3): return 2;
    if (s2 == 0): return 0;

    while (s1 % 2 == 0 and s1 != 0):
        s1 = s1 / 2
        cont += 1
    while (s2 % 2 == 0 and s2 != 0):
        s2 = s2 / 2
        cont -= 1
    if cont > 0 : return S + 1
    return S - 1

def main():
    S = int(stdin.readline())
    N = 0
    if S == 0:
        print (N)
        main()
    while S > N:
        cont = 0
        while S != 0:
            if ( S % 2 == 0):
                S = S/2
            else:
                S = phi(S)
            cont += 1
        print (cont)
        S = int(stdin.readline())
main()
