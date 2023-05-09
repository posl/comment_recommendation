def main():
    #入力
    N = int(input())
    mod = 998244353
    #dp[i][j][k] := i桁目までで条件を満たす数の個数で、i桁目はjで、i-1桁目との差はk
    dp = [[[0 for _ in range(3)] for _ in range(10)] for _ in range(N+1)]
    #初期化
    for i in range(1,10):
        dp[1][i][0] = 1
    for i in range(2,N+1):
        for j in range(10):
            for k in range(3):
                if j == 0:
                    dp[i][j][1] += dp[i-1][j+1][k]
                elif j == 9:
                    dp[i][j][1] += dp[i-1][j-1][k]
                else:
                    dp[i][j][0] += dp[i-1][j-1][k]
                    dp[i][j][2] += dp[i-1][j+1][k]
                dp[i][j][0] %= mod
                dp[i][j][1] %= mod
                dp[i][j][2] %= mod
    ans = 0
    for i in range(10):
        for j in range(3):
            ans += dp[N][i][j]
            ans %= mod
    print(ans)
