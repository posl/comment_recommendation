def solve(N):
    dp=[0]*(N+1)
    for i in range(1,N+1):
        dp[i]=dp[i-1]+1
        for j in range(1,i):
            if 6**j<=i:
                dp[i]=min(dp[i],dp[i-6**j]+1)
            if 9**j<=i:
                dp[i]=min(dp[i],dp[i-9**j]+1)
    return dp[N]
N=int(input())
print(solve(N))

if __name__ == '__main__':
    solve()