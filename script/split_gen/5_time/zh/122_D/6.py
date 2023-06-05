def main():
    N = int(input())
    #dp[i][j][k][l] := 长度为i，最后三个字母为jkl的字符串的数量
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
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
    #dp
    for i in range(4, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2:
                            continue
                        if k == 0 and j == 1 and m == 2:
                            continue
                        if k == 1 and l == 0 and m == 2:
                            continue
                        if j == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and m == 2:
                            continue
                        dp[i][k][l][m] += dp[i-1][j][k][l]
                        dp[i][k][l][m] %= 1000000007
    #答案
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= 1000000007
    print(ans)
