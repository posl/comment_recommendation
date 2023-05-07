def cmb(n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod
mod = 10**9+7
N, K = map(int, input().split())
fact = [1, 1] # fact[n] = (n! mod p)
factinv = [1, 1] # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1] # factinv 計算用
for i in range(2, N+K+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod//i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)
ans = 0
for i in range(min(K, N+1)):
    ans += cmb(N, i, mod) * cmb(N-1, i, mod)
    ans %= mod
print(ans)

if __name__ == '__main__':
    cmb()