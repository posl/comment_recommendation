def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = [list(map(int, input().split())) for _ in range(m)]
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        dp[i+1][0] = dp[i][0] + x[i]
    for i in range(n):
        for j in range(1, i+2):
            dp[i+1][j] = max(dp[i][j-1] + x[i], dp[i][j])
    ans = 0
    for i in range(m):
        for j in range(n+1):
            ans = max(ans, dp[j][j-y[i][0]] + y[i][1])
    print(ans)
