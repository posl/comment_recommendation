def comb(n, k, mod=10**9+7):
    if n < k:
        return 0
    k = min(k, n - k)
    x = 1
    y = 1
    for i in range(k):
        x = x * (n - i) % mod
        y = y * (k - i) % mod
    return x * pow(y, mod - 2, mod) % mod
N, K = map(int, input().split())
for i in range(1, K + 1):
    print(comb(K - 1, i - 1) * comb(N - K + 1, i) % (10**9 + 7))
