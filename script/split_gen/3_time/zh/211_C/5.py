def main():
    #S = input()
    S = "chchokudai"
    N = len(S)
    mod = 10**9 + 7
    # dp[i][j] means the number of ways to make "chokudai" from S[:i]
    dp = [[0 for _ in range(9)] for _ in range(N+1)]
    # init dp[0][0] = 1
    dp[0][0] = 1
    # dp[i][0] = 1
    for i in range(1, N+1):
        dp[i][0] = 1
    # dp[i][j] = dp[i-1][j] + dp[i-1][j-1] if S[i-1] == "chokudai"[j-1]
    for i in range(1, N+1):
        for j in range(1, 9):
            if S[i-1] == "chokudai"[j-1]:
                dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % mod
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][8])
