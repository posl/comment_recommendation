def main():
    N = int(input())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = min(dp[i - j**6] for j in range(1, 6) if i - j**6 >= 0) + 1
        dp[i] = min(dp[i], min(dp[i - j**9] for j in range(1, 5) if i - j**9 >= 0) + 1)
    print(dp[N])
