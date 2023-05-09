def main():
    N = int(input())
    # dp[i] = i円を引き出すのに必要な最小の回数
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        j = 1
        while i - 9 ** j >= 0:
            dp[i] = min(dp[i], dp[i - 9 ** j] + 1)
            j += 1
        j = 1
        while i - 6 ** j >= 0:
            dp[i] = min(dp[i], dp[i - 6 ** j] + 1)
            j += 1
        dp[i] = min(dp[i], dp[i - 1] + 1)
    print(dp[N])
