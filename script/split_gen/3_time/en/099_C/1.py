def main():
    N = int(input())
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for j in range(1, 6):
            if i - 6**j >= 0:
                dp[i] = min(dp[i], dp[i - 6**j] + 1)
        for j in range(1, 4):
            if i - 9**j >= 0:
                dp[i] = min(dp[i], dp[i - 9**j] + 1)
    print(dp[N])
