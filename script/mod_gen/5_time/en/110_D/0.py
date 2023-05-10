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
MOD = 10**9 + 7
factors = prime_factorize(M)
from collections import Counter
c = Counter(factors)
ans = 1
for i in c.values():
    ans *= pow(2, i-1, MOD)
    ans %= MOD
from math import factorial

if __name__ == '__main__':
    prime_factorize()