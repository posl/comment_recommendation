def main():
    N = int(input())
    MOD = 10**9+7
    # dp[i][j][k][l] := i 文字目までで j, k, l が最後に出てきた文字列の数
    dp = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i==0 and j==2 and k==1:
                    continue
                if i==0 and j==1 and k==2:
                    continue
                if i==2 and j==0 and k==1:
                    continue
                if i==0 and j==2 and k==0:
                    continue
                if i==2 and j==0 and k==0:
                    continue
                dp[i][j][k][0] = 1
    for i in range(N-1):
        ndp = [[[0]*4 for _ in range(4)] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j==0 and k==2 and m==1:
                            continue
                        if j==0 and k==1 and m==2:
                            continue
                        if j==2 and k==0 and m==1:
                            continue
                        if j==0 and k==2 and m==0:
                            continue
                        if j==2 and k==0 and m==0:
                            continue
                        ndp[k][l][m][0] += dp[j][k][l][0]
                        ndp[k][l][m][0] %= MOD
                        ndp[k][l][m][1] += dp[j][k][l][1]
                        ndp[k][l][m][1] %= MOD
                        ndp[k][l][m][2] += dp[j][k][l][2]
                        ndp[k][l][m][2] %= MOD
                        ndp[k][l][m][3] += dp[j][k][l][3]
                        ndp[k][l][m][3] %= MOD
                        if l==0 and m==2:
                            nd
