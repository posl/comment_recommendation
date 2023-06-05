def main():
    s = input()
    chokudaichokudai = 'chokudai'
    mod = 1000000007
    dp = [0] * 9
    dp[0] = 1
    for i in range(len(s)):
        for j in range(8, 0, -1):
            if s[i] == chokudaichokudai[j - 1]:
                dp[j] += dp[j - 1]
                dp[j] %= mod
    print(dp[8])

if __name__ == '__main__':
    main()