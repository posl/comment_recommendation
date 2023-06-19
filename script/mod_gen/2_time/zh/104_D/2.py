def main():
    s = input()
    n = len(s)
    mod = 10**9+7
    dp = [0]*8
    dp[0] = 1
    for i in range(n):
        if s[i] == 'A':
            dp[1] = (dp[1]+dp[0])%mod
        elif s[i] == 'B':
            dp[2] = (dp[2]+dp[1])%mod
        elif s[i] == 'C':
            dp[3] = (dp[3]+dp[2])%mod
        elif s[i] == '?':
            dp[3] = (dp[3]*3+dp[2])%mod
            dp[2] = (dp[2]*3+dp[1])%mod
            dp[1] = (dp[1]*3+dp[0])%mod
            dp[0] = dp[0]*3%mod
    print(dp[3])

if __name__ == '__main__':
    main()