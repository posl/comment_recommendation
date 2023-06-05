def main():
    s = input()
    chokudai = "chokudai"
    MOD = 10 ** 9 + 7
    dp = [0] * (len(chokudai) + 1)
    dp[0] = 1
    for c in s:
        for i, c2 in enumerate(chokudai):
            if c == c2:
                dp[i + 1] += dp[i]
                dp[i + 1] %= MOD
    print(dp[-1])

if __name__ == '__main__':
    main()