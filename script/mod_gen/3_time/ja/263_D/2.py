def main():
    N,L,R=map(int,input().split())
    A=list(map(int,input().split()))
    dp=[[0,0] for i in range(N+1)]
    for i in range(N):
        dp[i+1][0]=max(dp[i][0]+A[i]*L,dp[i][1]+A[i]*R)
        dp[i+1][1]=max(dp[i][0]+A[i]*R,dp[i][1]+A[i]*L)
    print(max(dp[N][0],dp[N][1]))

if __name__ == '__main__':
    main()