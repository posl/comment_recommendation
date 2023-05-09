def main():
    N = int(input())
    dp = [1000000] * (N + 1)
    dp[0] = 0
    for i in range(N):
        for j in range(6):
            if i + 6 ** j > N:
                break
            dp[i + 6 ** j] = min(dp[i + 6 ** j], dp[i] + 1)
        for j in range(9):
            if i + 9 ** j > N:
                break
            dp[i + 9 ** j] = min(dp[i + 9 ** j], dp[i] + 1)
    print(dp[N])
