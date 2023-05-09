def comb(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    return res
N, M, K = map(int, input().split())
mod = 998244353
ans = 0
for i in range(N + 1):
    for j in range(M + 1):
        if i * j > K:
            break
        ans += comb(N, i) * comb(N - i, j) * pow(M - j, N - i - 1, mod)
        ans %= mod
print(ans)
