def main():
    N = int(input())
    #dp[i][j][k] := i文字目までで、j文字目の直前にAGCが来ているか、k文字目の直前にAGCが来ているか
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    MOD = 10**9+7
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 2 and j == 0 and k == 1:
                    continue
                if i == 1 and j == 2 and k == 0:
                    continue
                dp[3][i][j] += 1
    for i in range(4, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 2 and l == 1:
                        continue
                    if j == 0 and k == 1 and l == 2:
                        continue
                    if j == 2 and k == 0 and l == 1:
                        continue
                    if j == 1 and k == 2 and l == 0:
                        continue
                    dp[i][j][k] += dp[i-1][k][l]
                    dp[i][j][k] %= MOD
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[N][i][j]
            ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()