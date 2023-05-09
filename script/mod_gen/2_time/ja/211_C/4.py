def main():
    S = input()
    mod = 10**9 + 7
    dp = [0] * 9
    dp[0] = 1
    for s in S:
        if s == "c":
            dp[1] += dp[0]
        elif s == "h":
            dp[2] += dp[1]
        elif s == "o":
            dp[3] += dp[2]
        elif s == "k":
            dp[4] += dp[3]
        elif s == "u":
            dp[5] += dp[4]
        elif s == "d":
            dp[6] += dp[5]
        elif s == "a":
            dp[7] += dp[6]
        elif s == "i":
            dp[8] += dp[7]
    print(dp[8] % mod)

if __name__ == '__main__':
    main()