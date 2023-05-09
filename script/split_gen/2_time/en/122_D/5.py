def main():
    n = int(input())
    dp = [[0]*4 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(4):
            for k in range(4):
                if j==0 and k==2: continue
                if j==0 and k==1: continue
                if j==1 and k==0: continue
                if j==2 and k==0: continue
                if j==1 and k==2: continue
                dp[i+1][k] += dp[i][j]
                dp[i+1][k] %= 1000000007
    print(sum(dp[n])%1000000007)
