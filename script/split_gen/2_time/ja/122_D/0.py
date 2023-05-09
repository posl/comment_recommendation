def main():
    N = int(input())
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if (j == 0 and k == 2 and m == 1) or (j == 0 and k == 1 and m == 2) or (j == 0 and l == 2 and m == 1) or (j == 2 and k == 0 and m == 1) or (l == 0 and k == 2 and m == 1):
                            continue
                        dp[i + 1][k][l][m] = (dp[i + 1][k][l][m] + dp[i][j][k][l]) % 1000000007
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans = (ans + dp[N][j][k][l]) % 1000000007
    print(ans)
