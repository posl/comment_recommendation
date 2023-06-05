def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = a[i]
    for j in range(1, m):
        for i in range(j, n):
            dp[i][j] = max(dp[k][j - 1] + a[i] * (i - k) for k in range(j - 1, i))
    print(max(dp[i][m - 1] for i in range(m - 1, n)))
