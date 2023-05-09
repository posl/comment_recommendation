def main():
    S = input()
    N = len(S)
    mod = 10**9+7
    dp = [0]*13
    dp[0] = 1
    for i in range(N):
        if S[i] != '?':
            tmp = [0]*13
            for j in range(13):
                tmp[(10*j+int(S[i]))%13] += dp[j]
        else:
            tmp = [0]*13
            for j in range(13):
                for k in range(10):
                    tmp[(10*j+k)%13] += dp[j]
        dp = [x%mod for x in tmp]
    print(dp[5])

if __name__ == '__main__':
    main()