def main():
    N = int(input())
    #dp[i][j][k][l]表示长度为i，最后三个字符为jkl的字符串的数量
    dp = [[[[0 for l in range(4)] for k in range(4)] for j in range(4)] for i in range(N+1)]
    #初始化
    dp[0][3][3][3] = 1
    mod = 10**9 + 7
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    #最后三个字符是jkl，检查倒数第二个字符
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2: continue
                        if k == 1 and l == 0 and m == 2: continue
                        if k == 0 and l == 2 and m == 1: continue
                        if j == 0 and l == 1 and m == 2: continue
                        if j == 0 and k == 1 and m == 2: continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= mod
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= mod
    print(ans)

if __name__ == '__main__':
    main()