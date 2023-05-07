def main():
    S = input()
    N = len(S)
    dp = [[0 for _ in range(2)] for _ in range(N+1)]
    for i in range(N):
        dp[i+1][0] = min(dp[i][0] + int(S[i]), dp[i][1] + 10 - int(S[i]))
        dp[i+1][1] = min(dp[i][0] + int(S[i]) + 1, dp[i][1] + 9 - int(S[i]))
    print(dp[N][0])
