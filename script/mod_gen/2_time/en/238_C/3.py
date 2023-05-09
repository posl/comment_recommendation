def solve(n):
    if n <= 9:
        return n * (n + 1) // 2
    else:
        d = len(str(n))
        ans = 0
        for i in range(1, d):
            ans += i * 9 * (10 ** (i - 1))
        ans += d * (n - (10 ** (d - 1)) + 1)
        return ans

if __name__ == '__main__':
    solve()