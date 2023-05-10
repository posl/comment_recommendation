def main():
    n, w = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    dp = [[0] * (w+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(w+1):
            if j - a[i] >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i][j-a[i]] + b[i])
            else:
                dp[i+1][j] = dp[i][j]
    print(dp[n][w])
