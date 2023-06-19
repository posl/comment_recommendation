def solve():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    #dp[i][j][k]表示前i种便当中选出j个章鱼烧和k个鱼形蛋糕的最小数量
    dp = [[[float('inf') for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        a, b = AB[i]
        for j in range(X+1):
            for k in range(Y+1):
                if j >= a and k >= b:
                    dp[i+1][j][k] = min(dp[i][j][k], dp[i][j-a][k-b]+1)
                else:
                    dp[i+1][j][k] = dp[i][j][k]
    if dp[N][X][Y] == float('inf'):
        print(-1)
    else:
        print(dp[N][X][Y])

if __name__ == '__main__':
    solve()