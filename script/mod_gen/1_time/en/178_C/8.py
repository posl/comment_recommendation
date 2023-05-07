def main():
    N = int(input())
    MOD = 10**9 + 7
    # dp[i][j][k] := i桁目までで条件を満たす数の個数
    # j: 0が存在するかどうか
    # k: 9が存在するかどうか
    dp = [[[0] * 2 for _ in range(2)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(2):
                for l in range(10):
                    ni = i + 1
                    nj = j
                    nk = k
                    if l == 0:
                        nj = 1
                    if l == 9:
                        nk = 1
                    dp[ni][nj][nk] += dp[i][j][k]
                    dp[ni][nj][nk] %= MOD
    ans = 0
    for j in range(2):
        for k in range(2):
            ans += dp[N][j][k]
            ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()