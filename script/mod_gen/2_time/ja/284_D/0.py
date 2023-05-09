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
T = int(input())
for i in range(T):
    N = int(input())
    p = prime_factorize(N)
    p = list(set(p))
    q = N // (p[0] ** 2)
    print(p[0],q)

if __name__ == '__main__':
    prime_factorize()