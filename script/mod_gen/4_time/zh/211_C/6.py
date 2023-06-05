def main():
    s = input()
    chokudai = "chokudai"
    dp = [0] * 9
    dp[0] = 1
    for i in range(len(s)):
        for j in range(8):
            if s[i] == chokudai[j]:
                dp[j + 1] += dp[j]
                dp[j + 1] %= 10 ** 9 + 7
    print(dp[8])

if __name__ == '__main__':
    main()