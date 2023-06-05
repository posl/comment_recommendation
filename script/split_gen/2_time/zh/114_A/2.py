def main():
    H,W,K = map(int,input().split())
    #print(H,W,K)
    ans = 0
    dp = [[0 for _ in range(W+1)] for _ in range(H+1)]
    dp[0][0] = 1
    MOD = 10**9+7
    for i in range(1,H+1):
        for j in range(W):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            dp[i][j] %= MOD
    #for i in range(H+1):
    #    print(dp[i])
    print(dp[H][K-1])
