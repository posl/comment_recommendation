def solve(N):
    # dp[i][j][k] = i桁目まで見て、0が出現したか、9が出現したか、その他の数字が出現したか
    # 0: 未出現
    # 1: 出現済み
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(N+1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(2):
            for k in range(3):
                for l in range(10):
                    if l == 0:
                        dp[i+1][1][k] += dp[i][j][k]
                    elif l == 9:
                        dp[i+1][j][2] += dp[i][j][k]
                    else:
                        dp[i+1][j][1] += dp[i][j][k]
    ans = 0
    for j in range(2):
        for k in range(3):
            ans += dp[N][j][k]
    return ans % (10**9+7)

if __name__ == '__main__':
    solve()