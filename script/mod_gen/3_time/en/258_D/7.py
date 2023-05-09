def main():
    N,X=map(int,input().split())
    A=[0]*(N+1)
    B=[0]*(N+1)
    for i in range(1,N+1):
        A[i],B[i]=map(int,input().split())
    dp=[[0]*(N+1) for i in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            dp[i][j]=min(dp[i-1][j]+A[i],dp[i-1][j-1]+A[i]+B[i])
    ans=10**18
    for i in range(N+1):
        ans=min(ans,dp[N][i]+(X-i)*B[N])
    print(ans)

if __name__ == '__main__':
    main()