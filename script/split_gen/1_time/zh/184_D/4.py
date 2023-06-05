def solve(a,b,c):
    dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    for i in range(99,-1,-1):
        for j in range(99,-1,-1):
            for k in range(99,-1,-1):
                if i+j+k == 0:
                    continue
                if i+j+k == 100:
                    continue
                dp[i][j][k] = (i*dp[i+1][j][k] + j*dp[i][j+1][k] + k*dp[i][j][k+1] + 100)/(i+j+k)
    return dp[a][b][c]
a,b,c = map(int,input().split())
print(solve(a,b,c))
