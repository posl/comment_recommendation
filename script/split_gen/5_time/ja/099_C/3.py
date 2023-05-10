def main():
    N = int(input())
    dp = [0] * (N+1)
    for i in range(N+1):
        dp[i] = i
    for i in range(1, N+1):
        j = 6
        while i - j >= 0:
            dp[i] = min(dp[i], dp[i-j] + 1)
            j *= 6
        j = 9
        while i - j >= 0:
            dp[i] = min(dp[i], dp[i-j] + 1)
            j *= 9
    print(dp[N])
