def main():
    N,W = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    #print(N,W,A,B)
    #dp[i][j]表示使用前i种奶酪，总重量为j时的最大美味值
    dp = [[0]*(W+1) for i in range(N+1)]
    for i in range(1,N+1):
        for j in range(W+1):
            if j < B[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-B[i-1]]+A[i-1]*B[i-1])
    #print(dp)
    print(dp[N][W])
