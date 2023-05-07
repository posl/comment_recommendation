def main():
    N = int(input())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(6, i + 1):
            dp[i] = min(dp[i], dp[i - j ** 6] + 1)
        for j in range(9, i + 1):
            dp[i] = min(dp[i], dp[i - j ** 9] + 1)
    print(dp[N])
