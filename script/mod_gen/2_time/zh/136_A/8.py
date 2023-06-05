def main():
    s = input()
    s = s[::-1]
    ans = 0
    mod = 10**9+7
    dp = [0]*13
    dp[0] = 1
    p = 1
    for c in s:
        if c == '?':
            dp2 = [0]*13
            for i in range(10):
                for j in range(13):
                    dp2[(j+i*p)%13] += dp[j]
                    dp2[(j+i*p)%13] %= mod
            dp = dp2
        else:
            dp2 = [0]*13
            for j in range(13):
                dp2[(j+int(c)*p)%13] += dp[j]
                dp2[(j+int(c)*p)%13] %= mod
            dp = dp2
        p *= 10
        p %= 13
    print(dp[5])

if __name__ == '__main__':
    main()