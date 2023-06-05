def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(n, x, y)
    #print(a)
    #print(b)
    #dp[i][j][k]表示前i种便当中选j个章鱼烧和k个鱼形蛋糕的最小便当数量
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if j >= a[i] and k >= b[i]:
                    dp[i+1][j][k] = min(dp[i][j][k], dp[i][j-a[i]][k-b[i]]+1)
                else:
                    dp[i+1][j][k] = dp[i][j][k]
    if dp[n][x][y] == float('inf'):
        print(-1)
    else:
        print(dp[n][x][y])
