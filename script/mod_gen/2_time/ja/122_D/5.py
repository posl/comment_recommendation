def main():
    #入力
    N = int(input())
    #文字列の数を10^9+7で割った余りを出力することをお忘れなく。
    MOD = 10**9 + 7
    #dp[i][j][k] := i文字目までで条件を満たす文字列の数で、
    #j文字目の前の文字がACGTの何番目か、
    #k文字目の前の文字がACGTの何番目か
    dp = [[[0]*4 for _ in range(4)] for _ in range(N+1)]
    #初期条件
    for i in range(4):
        for j in range(4):
            dp[3][i][j] = 1
    #文字列の数の計算
    for i in range(4, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    #AGCを部分文字列として含まない
                    if j == 0 and k == 2 and l == 1:
                        continue
                    #ACGT以外の文字を含まない
                    if l == 3:
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