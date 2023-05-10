def comb(n, r):
    if n < r:
        return 0
    if n == r:
        return 1
    if n - r < r:
        r = n - r
    over = 1
    under = 1
    for i in range(r):
        over *= n - i
        under *= i + 1
    return over // under
N, K = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
for i in range(K, N + 2):
    ans += comb(N + 1, i)
    ans %= mod
print(ans)
