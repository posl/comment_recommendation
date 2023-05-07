def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 1 and j == 0 and k == 2:
                    continue
                dp[3][i][j][k] = 1
    for i in range(3, N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if l == 0 and k == 1 and m == 2:
                            continue
                        if l == 0 and k == 2 and m == 1:
                            continue
                        if l == 1 and k == 0 and m == 2:
                            continue
                        if l == 1 and k == 2 and m == 0:
                            continue
                        if l == 2 and k == 0 and m == 1:
                            continue
                        if l == 2 and k == 1 and m == 0:
                            continue
                        dp[i+1][j][k][l] += dp[i][j][k][m]
                        dp[i+1][j][k][l] %= MOD
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()