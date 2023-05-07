def main():
    N = int(input())
    MOD = 10**9+7
    #dp[i][j][k][l] := i文字目まで見て、j文字目がACGTのどれか、k文字目がACGTのどれか、l文字目がACGTのどれかのときの場合の数
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
                if i==0 and j==2 and k==2:
                    continue
                if i==2 and j==0 and k==2:
                    continue
                dp[i][j][k][3] = 1
    for i in range(N-1):
        new_dp = [[[0]*4 for _ in range(4)] for _ in range(4)]
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if dp[j][k][l][3]==0:
                        continue
                    for m in range(4):
                        if j==0 and k==2 and m==1:
                            continue
                        if j==0 and k==1 and m==2:
                            continue
                        if j==2 and k==0 and m==1:
                            continue
                        if j==0 and k==2 and m==2:
                            continue
                        if j==2 and k==0 and m==2:
                            continue
                        new_dp[k][l][m][3] += dp[j][k][l][3]
                        new_dp[k][l][m][3] %= MOD
        dp = new_dp
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[i][j][k][3]
                ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()