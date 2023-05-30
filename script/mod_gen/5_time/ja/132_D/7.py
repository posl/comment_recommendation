def comb(n, r):
    if n < r:
        return 0
    if n == 0 or r == 0:
        return 1
    if n == r:
        return 1
    if r == 1:
        return n
    if r == 2:
        return n * (n - 1) // 2
    return comb(n - 1, r - 1) + comb(n - 1, r)
N, K = map(int, input().split())
for i in range(1, K + 1):
    if N - K + 1 < i:
        print(0)
    else:
        print(comb(N - K + 1, i) * comb(K - 1, i - 1) % (10 ** 9 + 7))
