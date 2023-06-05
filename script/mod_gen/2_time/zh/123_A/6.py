def main():
    n = int(input())
    mod = 10**9 + 7
    #dp[i][j][k][l]表示长度为i，最后三个字母为jkl的字符串的数量
    dp = [[[[0]*4 for i in range(4)] for j in range(4)] for k in range(n+1)]
    #初始化
    dp[0][3][3][3] = 1
    for i in range(1, n+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if (j==1 and k==2 and m==3) or (j==1 and l==2 and m==3) or (k==1 and l==2 and m==3) or (j==2 and k==1 and m==3) or (j==1 and k==3 and m==2):
                            continue
                        dp[i][k][l][m] += dp[i-1][j][k][l]
                        dp[i][k][l][m] %= mod
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[n][j][k][l]
                ans %= mod
    print(ans)

if __name__ == '__main__':
    main()