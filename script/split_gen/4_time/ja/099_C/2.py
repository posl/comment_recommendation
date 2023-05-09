def main():
    N = int(input())
    dp = [100000] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(1, 7):
            if i - pow(6, j) >= 0:
                dp[i] = min(dp[i], dp[i - pow(6, j)] + 1)
        for j in range(1, 7):
            if i - pow(9, j) >= 0:
                dp[i] = min(dp[i], dp[i - pow(9, j)] + 1)
    print(dp[N])
