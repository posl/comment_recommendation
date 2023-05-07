def main():
    N = int(input())
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        for j in range(6):
            if i + 6 ** j <= N:
                dp[i + 6 ** j] = min(dp[i + 6 ** j], dp[i] + 1)
        for j in range(9):
            if i + 9 ** j <= N:
                dp[i + 9 ** j] = min(dp[i + 9 ** j], dp[i] + 1)
    print(dp[N])
