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
N, M = map(int, input().split())
mod = 10**9 + 7
ans = 1
for i in range(1, M + 1):
    ans *= i
    ans %= mod
pf = prime_factorize(ans)
pf = list(set(pf))
ans = 1
for i in pf:
    ans *= (pf.count(i) + 1)
    ans %= mod
print(ans)
