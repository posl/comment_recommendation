def main():
    s = input()
    n = len(s)
    mod = 10**9 + 7
    dp = [[0]*4 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        if s[i] == 'A':
            dp[i+1][0] = (dp[i][0]*3+dp[i][1])%mod
            dp[i+1][1] = dp[i][1]
            dp[i+1][2] = dp[i][2]
            dp[i+1][3] = (dp[i][3]*3+dp[i][2])%mod
        elif s[i] == 'B':
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = (dp[i][0]+dp[i][1]*3)%mod
            dp[i+1][2] = dp[i][2]
            dp[i+1][3] = (dp[i][3]*3+dp[i][2])%mod
        elif s[i] == 'C':
            dp[i+1][0] = dp[i][0]
            dp[i+1][1] = dp[i][1]
            dp[i+1][2] = (dp[i][0]+dp[i][2]*3)%mod
            dp[i+1][3] = (dp[i][3]*3+dp[i][2])%mod
        else:
            dp[i+1][0] = (dp[i][0]*3+dp[i][1])%mod
            dp[i+1][1] = (dp[i][0]+dp[i][1]*3)%mod
            dp[i+1][2] = (dp[i][0]+dp[i][2]*3)%mod
            dp[i+1][3] = (dp[i][3]*3+dp[i][2])%mod
    print(dp[n][3])
