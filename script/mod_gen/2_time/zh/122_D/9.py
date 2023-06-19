def main():
    n = int(input())
    mod = 10**9 + 7
    #dp[i][j][k][l] 表示长度为i，末尾三个字母分别为j,k,l的字符串数量
    dp = [[[[0 for i in range(4)] for i in range(4)] for i in range(4)] for i in range(n+1)]
    dp[0][3][3][3] = 1
    for i in range(n):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    #最后两个字母为AG时，末尾为C的情况
                    if j == 0 and k == 1 and l == 2:
                        continue
                    #最后两个字母为GA时，末尾为C的情况
                    if j == 1 and k == 0 and l == 2:
                        continue
                    #最后一个字母为A，且倒数第二个字母为GC时，末尾为C的情况
                    if j == 0 and k == 2 and l == 1:
                        continue
                    #最后一个字母为A，且倒数第二个字母为G时，末尾为C的情况
                    if j == 0 and k == 1 and l == 2:
                        continue
                    #最后一个字母为A，且倒数第二个字母为C时，末尾为G的情况
                    if j == 0 and k == 2 and l == 1:
                        continue
                    dp[i+1][k][l][j] += dp[i][j][k][l]
                    dp[i+1][k][l][j] %= mod
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[n][j][k][l]
                ans %= mod
    print(ans)
main()
