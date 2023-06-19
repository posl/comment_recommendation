def main():
    n = int(input())
    mod = 10**9+7
    # dp[i][j][k][l] は, i文字目までに, jが末尾に続く, kが末尾から2番目に続く, lが末尾から3番目に続く文字列の個数
    dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
    dp[0][3][3][3] = 1
    for i in range(n):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k==1 and l==2 and m==3: continue
                        if k==2 and l==1 and m==3: continue
                        if k==1 and l==3 and m==2: continue
                        if j==1 and l==2 and m==3: continue
                        if j==1 and k==2 and m==3: continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= mod
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[n][j][k][l]
                ans %= mod
    print(ans)
