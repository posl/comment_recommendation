def main():
    N = int(input())
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + 1
        for j in range(6):
            if i - 6 ** j < 0:
                break
            dp[i] = min(dp[i], dp[i - 6 ** j] + 1)
        for j in range(9):
            if i - 9 ** j < 0:
                break
            dp[i] = min(dp[i], dp[i - 9 ** j] + 1)
    print(dp[N])
