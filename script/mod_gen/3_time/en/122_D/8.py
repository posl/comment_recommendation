def main():
    N = int(input())
    MOD = 10**9 + 7
    # 0: A, 1: C, 2: G, 3: T
    # dp[i][j][k][l] := i文字目までで、j文字目がACGとなるようにしているか(0: ない, 1: ある)、
    #                   j文字目がACGのどこにあるか(0: A, 1: C, 2: G)、
    #                   j文字目の前の文字がk、j文字目の次の文字がl
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == 0 and k == 1 and l == 2: continue
                        if j == 0 and k == 2 and l == 1: continue
                        if j == 1 and k == 0 and l == 2: continue
                        if j == 1 and k == 2 and l == 0: continue
                        if j == 2 and k == 0 and l == 1: continue
                        if j == 2 and k == 1 and l == 0: continue
                        if j == 0 and l == 2 and m == 1: continue
                        if j == 0 and l == 1 and m == 2: continue
                        if j == 1 and l == 2 and m == 0: continue
                        if j == 1 and l == 0 and m == 2: continue
                        if j == 2 and l == 0 and m == 1: continue
                        if j == 2 and l == 1 and m == 0: continue
                        dp[i + 1][j == 3][l][m] += dp[i][j][k][l]
                        dp[i + 1][j

if __name__ == '__main__':
    main()