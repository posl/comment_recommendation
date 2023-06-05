def main():
    #读取输入
    n = int(input())
    x, y = map(int, input().split())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    #动态规划
    #dp[i][j][k]表示前i个便当中，使用j个章鱼烧，k个鱼形蛋糕的最小便当数
    dp = [[[float('inf')]*(y+1) for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                if j+a[i] <= x and k+b[i] <= y:
                    dp[i+1][j+a[i]][k+b[i]] = min(dp[i+1][j+a[i]][k+b[i]], dp[i][j][k]+1)
    if dp[n][x][y] == float('inf'):
        print(-1)
    else:
        print(dp[n][x][y])
