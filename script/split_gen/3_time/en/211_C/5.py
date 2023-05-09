def main():
    S = input()
    mod = 10**9 + 7
    dp = [0]*8
    for s in S:
        if s == 'c':
            dp[0] = (dp[0] + 1) % mod
        elif s == 'h':
            dp[1] = (dp[1] + dp[0]) % mod
        elif s == 'o':
            dp[2] = (dp[2] + dp[1]) % mod
        elif s == 'k':
            dp[3] = (dp[3] + dp[2]) % mod
        elif s == 'u':
            dp[4] = (dp[4] + dp[3]) % mod
        elif s == 'd':
            dp[5] = (dp[5] + dp[4]) % mod
        elif s == 'a':
            dp[6] = (dp[6] + dp[5]) % mod
        elif s == 'i':
            dp[7] = (dp[7] + dp[6]) % mod
    print(dp[7])
main()
