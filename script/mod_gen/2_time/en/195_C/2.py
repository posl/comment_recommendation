def solve(n):
    ans = 0
    i = 1
    while i <= n:
        ans += (n - i + 1)
        i *= 1000
    return ans

if __name__ == '__main__':
    solve()