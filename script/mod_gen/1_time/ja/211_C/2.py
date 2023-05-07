def main():
    S = input()
    MOD = 10**9 + 7
    dp = [0] * 8
    for s in S:
        if s == 'c':
            dp[0] += 1
        elif s == 'h':
            dp[1] += dp[0]
        elif s == 'o':
            dp[2] += dp[1]
        elif s == 'k':
            dp[3] += dp[2]
        elif s == 'u':
            dp[4] += dp[3]
        elif s == 'd':
            dp[5] += dp[4]
        elif s == 'a':
            dp[6] += dp[5]
        elif s == 'i':
            dp[7] += dp[6]
    print(dp[7] % MOD)

if __name__ == '__main__':
    main()