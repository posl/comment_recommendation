def main():
    s = input()
    t = 'atcoder'
    dp = [0] * (len(t) + 1)
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[j + 1] = max(dp[j + 1], dp[j] + 1)
            dp[j + 1] = max(dp[j + 1], dp[j])
    print(len(s) - dp[-1])

if __name__ == '__main__':
    main()