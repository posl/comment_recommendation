def prime_factorize(n):
    res = []
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            ex = 0
            while n%i==0:
                ex += 1
                n //= i
            res.append([i, ex])
    if n!=1:
        res.append([n, 1])
    return res
n,m = map(int, input().split())
mod = 10**9+7
ans = 1
for p, e in prime_factorize(m):
    ans *= comb(e+n-1, e, mod)
    ans %= mod
print(ans)
