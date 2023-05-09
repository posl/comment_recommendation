def nCk(n, k):
    if n < k:
        return 0
    if k == 0:
        return 1
    return n * nCk(n-1, k-1) // k
n, a, b = map(int, input().split())
mod = 10**9 + 7
print((pow(2, n, mod) - 1 - nCk(n, a) - nCk(n, b)) % mod)
