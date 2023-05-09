def main():
    s = input()
    #s = '7?4'
    l = len(s)
    dp = [[0]*13 for _ in range(l+1)]
    dp[0][0] = 1
    for i in range(l):
        for j in range(10):
            if s[i] != '?' and str(j) != s[i]:
                continue
            for k in range(13):
                dp[i+1][(k*10+j)%13] += dp[i][k]
    print(dp[l][5] % (10**9+7))

if __name__ == '__main__':
    main()