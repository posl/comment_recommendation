def main():
    S = input()
    mod = 10**9+7
    N = len(S)
    dp = [[0]*4 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(4):
            if S[i] == "?":
                dp[i+1][j] = dp[i][j]*3
            else:
                dp[i+1][j] = dp[i][j]
        if S[i] == "A" or S[i] == "?":
            dp[i+1][1] += dp[i][0]
        if S[i] == "B" or S[i] == "?":
            dp[i+1][2] += dp[i][1]
        if S[i] == "C" or S[i] == "?":
            dp[i+1][3] += dp[i][2]
        for j in range(4):
            dp[i+1][j] %= mod
    print(dp[N][3])
