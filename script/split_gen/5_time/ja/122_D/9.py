def main():
    n = int(input())
    #dp[i][j][k][l] := i文字目まで決めた時、末尾から3文字目までがj,k,lであるような文字列の個数
    dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
    #初期条件
    dp[0][3][3][3] = 1
    mod = 10**9+7
    #文字列の長さ
    for i in range(n):
        #末尾から3文字目
        for j in range(4):
            #末尾から2文字目
            for k in range(4):
                #末尾から1文字目
                for l in range(4):
                    #末尾から3文字目がAの時
                    for m in range(4):
                        #AGCを含まない時
                        if k == 0 and l == 1 and m == 2:
                            continue
                        #AGCを含まない時
                        if k == 1 and l == 0 and m == 2:
                            continue
                        #AGCを含まない時
                        if k == 0 and l == 2 and m == 1:
                            continue
                        #末尾から3文字目がAの時
                        if j == 0 and l == 1 and m == 2:
                            continue
                        #末尾から3文字目がAの時
                        if j == 0 and k == 1 and m == 2:
                            continue
                        dp[i+1][k][l][m] += dp[i][j][k][l]
                        dp[i+1][k][l][m] %= mod
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[n][i][j][k]
                ans %= mod
    print(ans)
