def main():
    S = input()
    n = len(S)
    mod = 10**9 + 7
    chokudai = 'chokudai'
    dp = [[0 for i in range(n+1)] for j in range(8+1)]
    for i in range(n+1):
        dp[0][i] = 1
    for i in range(1,8+1):
        for j in range(1,n+1):
            if S[j-1] == chokudai[i-1]:
                dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) % mod
            else:
                dp[i][j] = dp[i][j-1]
    print(dp[8][n])
