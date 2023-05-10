def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    
    for i in range(N):
        A[i] += A[i-1]
    
    dp = [[float("inf")]*2 for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        dp[i+1][0] = min(dp[i+1][0], dp[i][0]+A[i]*R+A[i-1]*(L-R))
        dp[i+1][0] = min(dp[i+1][0], dp[i][1]+A[i]*R+A[i-1]*(L-R))
        dp[i+1][1] = min(dp[i+1][1], dp[i][0]+A[i]*L+A[i-1]*(R-L))
        dp[i+1][1] = min(dp[i+1][1], dp[i][1]+A[i]*L+A[i-1]*(R-L))
    
    print(dp[N][0])

if __name__ == '__main__':
    main()