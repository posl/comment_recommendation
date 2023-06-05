def main():
    n = int(input())
    mod = 1000000007
    dp = [[[[0 for i in range(4)] for j in range(4)] for k in range(4)] for l in range(n+1)]
    dp[0][3][3][3] = 1
    for i in range(n):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if dp[i][j][k][l] == 0:
                        continue
                    for m in range(4):
                        if k == 0 and l == 1 and m == 2:
                            continue
                        if k == 1 and l == 0 and m == 2:
                            continue
                        if k == 0 and l == 2 and m == 1:
                            continue
                        if j == 0 and l == 1 and m == 2:
                            continue
                        if j == 0 and k == 1 and m == 2:
                            continue
                        dp[i+1][k][l][m] = (dp[i+1][k][l][m] + dp[i][j][k][l]) % mod
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans = (ans + dp[n][j][k][l]) % mod
    print(ans)
