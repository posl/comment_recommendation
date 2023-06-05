def solve(n,v,c):
    dp = [[0]*(n+1) for _ in range(51)]
    for i in range(1,n+1):
        for j in range(51):
            if j < c[i-1]:
                dp[j][i] = dp[j][i-1]
            else:
                dp[j][i] = max(dp[j][i-1],dp[j-c[i-1]][i-1]+v[i-1])
    return dp[50][n]
n = int(input())
v = list(map(int,input().split()))
c = list(map(int,input().split()))
print(solve(n,v,c))
