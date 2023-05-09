def solve():
    n = int(input())
    a = []
    for i in range(n):
        t, x, a = map(int, input().split())
        a.append((t, x, a))
    a.sort()
    dp = [[0] * 5 for i in range(n + 1)]
    for i in range(n):
        t, x, a = a[i]
        for j in range(5):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j == x:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + a)
            if abs(j - x) <= t - i:
                dp[i + 1][x] = max(dp[i + 1][x], dp[i][j] + a)
    print(max(dp[n]))

if __name__ == '__main__':
    solve()