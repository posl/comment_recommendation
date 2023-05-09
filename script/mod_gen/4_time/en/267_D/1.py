def solve(n, m, a):
    a.sort(reverse=True)
    dp = [[-float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j] != -float('inf'):
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
                if j + 1 <= m:
                    dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + a[i] * (j + 1))
    return dp[n][m]
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))

if __name__ == '__main__':
    solve()