def main():
    N,W = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    #print(N,W)
    #print('-----')
    #dp[i][j]表示前i种奶酪总重量为j时的最大美味值
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(W+1):
            if j-B[i] >= 0:
                dp[i+1][j] = max(dp[i][j], dp[i+1][j-B[i]]+A[i])
            else:
                dp[i+1][j] = dp[i][j]
    #print(dp)
    print(dp[N][W])

if __name__ == '__main__':
    main()