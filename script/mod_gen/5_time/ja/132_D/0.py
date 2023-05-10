def combination_mod(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod
mod = 10**9 + 7
N, K = map(int, input().split())
fact = [1, 1] #fact[n] = (n! mod p)
factinv = [1, 1] #factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1] #inv[n] = (n^(-1) mod p)
for i in range(2, N+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)
for i in range(1, K+1):
    ans = combination_mod(N-K+1, i, mod) * combination_mod(K-1, i-1, mod)
    ans %= mod
    print(ans)

if __name__ == '__main__':
    combination_mod()