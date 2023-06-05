def comb(n, r, mod=10**9+7):
    if r > n - r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n % mod
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] // = pivot
                denominator[k] // = pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result = result * numerator[k] % mod
    return result
n, a, b = map(int, input().split())
mod = 10**9+7
print((pow(2, n, mod) - 1 - comb(n, a, mod) - comb(n, b, mod)) % mod)
