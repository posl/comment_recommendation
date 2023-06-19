def solve(A,B,K):
    def dfs(a,b,k):
        if a==0:
            return 'b'*b
        elif b==0:
            return 'a'*a
        elif k<=dp[a-1][b]:
            return 'a'+dfs(a-1,b,k)
        else:
            return 'b'+dfs(a,b-1,k-dp[a-1][b])
    dp=[[1]*(B+1) for _ in range(A+1)]
    for i in range(1,A+1):
        for j in range(1,B+1):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dfs(A,B,K)
A,B,K=map(int,input().split())
print(solve(A,B,K))
