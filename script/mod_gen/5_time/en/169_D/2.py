def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
N = int(input())
A = prime_factorize(N)
B = list(set(A))
C = list(set(A))
D = list(set(A))
E = []
for i in range(len(B)):
    for j in range(len(C)):
        for k in range(len(D)):
            E.append(B[i]*C[j]*D[k])
F = list(set(E))
G = []
for i in range(len(F)):
    G.append(N//F[i])
H = list(set(G))
print(len(H)-1)

if __name__ == '__main__':
    prime_factorize()