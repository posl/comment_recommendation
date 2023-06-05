def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    cy = [list(map(int, input().split())) for _ in range(m)]
    c = [i[0] for i in cy]
    y = [i[1] for i in cy]
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + 1 in c:
                dp[i + 1][1] = max(dp[i + 1][1], dp[i][j] + y[c.index(j + 1)])
    print(max(dp[n]))
