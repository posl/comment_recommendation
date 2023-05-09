def combination(n, r, mod=998244353):
    if n < r: 
        return 0
    if r == 0: 
        return 1
    if r > n - r: 
        r = n - r
    return fact[n] * factinv[r] * factinv[n-r] % mod
N, M, K = map(int, input().split())
fact = [1, 1] 
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N*M+1):
    fact.append((fact[-1] * i) % 998244353)
    inv.append((-inv[998244353 % i] * (998244353//i)) % 998244353)
    factinv.append((factinv[-1] * inv[-1]) % 998244353)
ans = 0
for i in range(1, M+1):
    ans += combination(N*M-i, N-1) * pow(i, N, 998244353)
    ans %= 998244353
print(ans)
