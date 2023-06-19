def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    #dp[i][j][k][l]表示长度为i，最后三个字母为j,k,l的字符串的数量
    #j,k,l为0,1,2,3,分别表示A,C,G,T
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    #初始化
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if j == 0 and k == 1 and l == 2:
                    continue
                if j == 0 and k == 2 and l == 1:
                    continue
                if j == 1 and k == 0 and l == 2:
                    continue
                dp[3][j][k][l] = 1
    for i in range(4, N + 1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2:
                            continue
                        if k == 0 and l == 2 and m == 1:
                            continue
                        if j == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and l == 2:
                            continue
                        dp[i][k][l][m] = (dp[i][k][l][m] + dp[i - 1][j][k][l]) % MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans = (ans + dp[N][j][k][l]) % MOD
    print(ans)
