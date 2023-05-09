def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    numer = 1  # 分子
    denom = 1  # 分母
    for i in range(1, r + 1):
        numer = numer * (n + 1 - i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod - 2, mod) % mod
mod = 10**9+7
n, k = map(int, input().split())
print(cmb(n+k, k, mod))
