def comb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod
N, K = map(int, input().split())
mod = 10**9+7
N += 1
fact = [1, 1] # 階乗を格納するリスト
factinv = [1, 1] # 階乗の逆元を格納するリスト
inv = [0, 1] # 逆元を計算するためのリスト
for i in range(2, N+K+1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod//i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)
result = 0
for i in range(K, N+1):
    result += comb(N, i, mod) * comb(N-1, i-1, mod)
    result %= mod
print(result)

if __name__ == '__main__':
    comb()