def combinations_count(n, r):
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= numerator[k]
    return result
n, a, b = map(int, input().split())
mod = 10**9 + 7
total = pow(2, n, mod) - 1
a_count = combinations_count(n, a)
b_count = combinations_count(n, b)
print((total - a_count - b_count) % mod)
