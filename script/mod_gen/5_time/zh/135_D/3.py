def main():
    S = input()
    S = S[::-1]
    dp = [0] * 13
    dp[0] = 1
    base = 1
    for s in S:
        if s == "?":
            dp2 = [0] * 13
            for i in range(10):
                for j in range(13):
                    dp2[(i * base + j) % 13] += dp[j]
            dp = dp2
        else:
            s = int(s)
            dp2 = [0] * 13
            for j in range(13):
                dp2[(s * base + j) % 13] += dp[j]
            dp = dp2
        base *= 10
        base %= 13
        for i in range(13):
            dp[i] %= (10 ** 9 + 7)
    print(dp[5])

if __name__ == '__main__':
    main()