def solve():
    a,b,c = map(int, input().split())
    dp = [[[0.0]*(101) for _ in range(101)] for _ in range(101)]
    for i in range(99, -1, -1):
        for j in range(99, -1, -1):
            for k in range(99, -1, -1):
                if i+j+k == 0:
                    continue
                dp[i][j][k] = (dp[i+1][j][k]+1)*i/(i+j+k) + (dp[i][j+1][k]+1)*j/(i+j+k) + (dp[i][j][k+1]+1)*k/(i+j+k)
    print(dp[a][b][c])
