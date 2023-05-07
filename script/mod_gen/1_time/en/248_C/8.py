def comb(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    if n == 0 or r == 0 or n == r:
        return 1
    if n - r < r:
        r = n - r
    c = 1
    for i in range(r):
        c = c * (n - i) // (i + 1)
    return c
n, m, k = map(int, input().split())
mod = 998244353
ans = 0
for i in range(n):
    ans += comb(n - 1, i) * m * pow(m - 1, n - i - 1, mod)
    ans %= mod
print(ans)

if __name__ == '__main__':
    comb()