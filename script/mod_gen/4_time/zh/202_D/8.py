def dfs(a,b,k):
    if a == 0:
        return "b"*b
    elif b == 0:
        return "a"*a
    elif k <= dp[a-1][b]:
        return "a" + dfs(a-1,b,k)
    else:
        return "b" + dfs(a,b-1,k-dp[a-1][b])
a,b,k = map(int,input().split())
dp = [[0 for _ in range(b+1)] for _ in range(a+1)]
dp[0][0] = 1
for i in range(a+1):
    for j in range(b+1):
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
print(dfs(a,b,k))
