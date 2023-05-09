def main():
    N = int(input())
    MOD = 10**9+7
    # dp[i][j][k][l] は、長さ i の文字列のうち、末尾が [j][k][l] であるものの個数
    # j: Aの個数
    # k: Cの個数
    # l: Gの個数
    # に対応
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    dp[0][0][0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == 0 and k == 2 and m == 1:
                            continue
                        if j == 0 and l == 2 and m == 1:
                            continue
                        if k == 0 and l == 2 and m == 1:
                            continue
                        if j == 1 and k == 0 and m == 2:
                            continue
                        if j == 1 and l == 0 and m == 2:
                            continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)
