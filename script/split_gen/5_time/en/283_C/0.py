def main():
    S = input()
    N = len(S)
    dp = [[float('inf') for _ in range(2)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        s = int(S[i])
        dp[i+1][0] = min(dp[i+1][0], dp[i][0]+s, dp[i][1]+s+1)
        dp[i+1][1] = min(dp[i+1][1], dp[i][0]+s+1, dp[i][1]+s)
    print(dp[N][0])
