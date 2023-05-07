def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0] * m
    y = [0] * m
    for i in range(m):
        c[i], y[i] = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + x[i - 1]
        for j in range(m):
            if i - c[j] >= 0:
                dp[i] = max(dp[i], dp[i - c[j]] + y[j])
    print(dp[n])
