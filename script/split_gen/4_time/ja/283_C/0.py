def main():
    S = input()
    N = len(S)
    dp = [[float('inf')] * 2 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[i+1][0] = min(dp[i+1][0], dp[i][0] + int(S[i]))
        dp[i+1][0] = min(dp[i+1][0], dp[i][1] + int(S[i]) + 1)
        dp[i+1][1] = min(dp[i+1][1], dp[i][0] + (10 - int(S[i]) - 1))
        dp[i+1][1] = min(dp[i+1][1], dp[i][1] + (10 - int(S[i])))
    print(min(dp[N][0], dp[N][1] + 1))
