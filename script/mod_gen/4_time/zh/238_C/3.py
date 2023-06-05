def solve(n):
    mod = 998244353
    ans = 0
    x = 1
    while x <= n:
        y = min(n, x * 10 - 1)
        ans += (x + y) * (y - x + 1) // 2 * len(str(x))
        ans %= mod
        x *= 10
    return ans

if __name__ == '__main__':
    solve()