def main():
    N = int(input())
    mod = 10**9 + 7
    dp = [[[[0] * 4 for i in range(4)] for j in range(4)] for k in range(N+1)]
    # dp[i][j][k][l] := i文字目までで最後の3文字がjklとなる文字列の数
    # j, k, l = 0, 1, 2, 3 は A, C, G, T に対応
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if j == 0 and k == 1 and l == 2: continue
                if j == 0 and k == 2 and l == 1: continue
                if j == 1 and k == 0 and l == 2: continue
                dp[3][j][k][l] = 1
    for i in range(4, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2: continue
                        if k == 0 and j == 1 and m == 2: continue
                        if j == 0 and k == 1 and m == 2: continue
                        if k == 0 and l == 2 and m == 1: continue
                        if k == 0 and l == 1 and m == 2: continue
                        dp[i][j][k][l] += dp[i-1][k][l][m]
                        dp[i][j][k][l] %= mod
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= mod
    print(ans)
