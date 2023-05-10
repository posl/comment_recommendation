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
t = int(input())
for _ in range(t):
    n = int(input())
    a = prime_factorize(n)
    p = a[0]
    for i in range(1, len(a)):
        if a[i] != p:
            q = a[i]
            break
    print(p, q)
