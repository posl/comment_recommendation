def main():
    N = int(input())
    MOD = 10**9 + 7
    # dp[i][j][k][l] = i文字目までで、j文字目がAGCのA、k文字目がAGCのG、l文字目がAGCのCである文字列の数
    dp = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 2 and j == 0 and k == 1:
                    continue
                dp[i][j][k] = 1
    for _ in range(N-3):
        ndp = [[[0]*4 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if j == 0 and k == 2 and l == 1:
                            continue
                        if j == 0 and k == 1 and l == 2:
                            continue
                        if j == 2 and k == 0 and l == 1:
                            continue
                        ndp[j][k][l] += dp[i][j][k]
                        ndp[j][k][l] %= MOD
        dp = ndp
    print(sum([sum([sum(dp[i][j]) for j in range(4)]) for i in range(4)]) % MOD)

if __name__ == '__main__':
    main()