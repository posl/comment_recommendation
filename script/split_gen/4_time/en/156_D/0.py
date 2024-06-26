def comb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % mod
mod = 10**9+7
N = 2*10**5+1
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod%i] * (mod//i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)
n, a, b = map(int, input().split())
ans = pow(2, n, mod) - 1 - comb(n, a, mod) - comb(n, b, mod)
print(ans%mod)
