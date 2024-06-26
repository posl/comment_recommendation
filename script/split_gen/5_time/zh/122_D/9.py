def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    #dp[i][j][k][l] は、長さiの文字列で、末尾から3文字がjklであるものの個数を表す
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    #初期値
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
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
                        dp[i + 1][k][l][m] += dp[i][j][k][l]
                        dp[i + 1][k][l][m] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)
