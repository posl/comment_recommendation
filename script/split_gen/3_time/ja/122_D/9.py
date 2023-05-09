def main():
    N = int(input())
    MOD = 10**9+7
    dp = [[[0]*4 for i in range(4)] for j in range(N+1)]
    #dp[i][j][k]はi番目の文字がAGCTのj番目の文字で、i-1番目の文字がAGCTのk番目の文字の時の文字列の数
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i==0 and j==1 and k==2:
                    dp[3][i][j] = 0
                elif i==0 and j==2 and k==1:
                    dp[3][i][j] = 0
                elif i==1 and j==0 and k==2:
                    dp[3][i][j] = 0
                elif i==1 and j==2 and k==0:
                    dp[3][i][j] = 0
                elif i==2 and j==0 and k==1:
                    dp[3][i][j] = 0
                elif i==2 and j==1 and k==0:
                    dp[3][i][j] = 0
                else:
                    dp[3][i][j] = 1
    for i in range(3,N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j==0 and k==1 and l==2:
                        dp[i+1][k][l] += dp[i][j][k]
                    elif j==0 and k==2 and l==1:
                        dp[i+1][k][l] += dp[i][j][k]
                    elif j==1 and k==0 and l==2:
                        dp[i+1][k][l] += dp[i][j][k]
                    elif j==1 and k==2 and l==0:
                        dp[i+1][k][l] += dp[i][j][k]
                    elif j==2 and k==0 and l==1:
                        dp[i+1][k][l] += dp[i][j][k]
                    elif j==2 and k==1 and l==0:
