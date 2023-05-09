def main():
    N = int(input())
    # dp[i] = i yen can be withdrawn in dp[i] operations
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        for j in range(6):
            if i - 6 ** j >= 0:
                dp[i] += dp[i - 6 ** j]
        for j in range(9):
            if i - 9 ** j >= 0:
                dp[i] += dp[i - 9 ** j]
    print(dp[N])
