def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = [0] * m
    y = [0] * m
    for i in range(m):
        c[i], y[i] = map(int, input().split())
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = max(dp[i], dp[i + 1])
        for j in range(m):
            if i + 1 >= c[j]:
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - c[j]] + y[j])
        dp[i + 1] += x[i]
    print(dp[n])
