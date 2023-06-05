def main():
    N = int(input())
    MOD = 10**9+7
    #dp[i][j][k][l] := 长度为iで末尾3文字がjklである文字列の個数
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    #初期化
    for j in range(4):
        for k in range(4):
            for l in range(4):
                if j==0 and k==1 and l==2:
                    continue
                if j==0 and k==2 and l==1:
                    continue
                if j==1 and k==0 and l==2:
                    continue
                dp[3][j][k][l] = 1
    for i in range(4,N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if k==0 and l==1 and m==2:
                            continue
                        if k==0 and l==2 and m==1:
                            continue
                        if j==0 and l==1 and m==2:
                            continue
                        if k==0 and j==1 and m==2:
                            continue
                        if k==0 and l==1 and j==2:
                            continue
                        dp[i][k][l][m] += dp[i-1][j][k][l]
                        dp[i][k][l][m] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            for l in range(4):
                ans += dp[N][j][k][l]
                ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()