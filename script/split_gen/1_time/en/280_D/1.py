def prime_factorization(n):
    pf = {}
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            pf[i] = pf.get(i, 0) + 1
            n //= i
    if n != 1:
        pf[n] = pf.get(n, 0) + 1
    return pf
k = int(input())
pf = prime_factorization(k)
ans = 1
for p in pf:
    ans *= p ** (pf[p] // len(str(p)))
print(ans)
