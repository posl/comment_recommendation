def main():
    N = int(input())
    X, Y = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[float('inf')] * (X+1) for _ in range(Y+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        a, b = AB[i]
        for j in range(Y+1):
            for k in range(X+1):
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                if j - b >= 0 and k - a >= 0:
                    dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j-b][k-a]+1)
    if dp[N][Y][X] == float('inf'):
        print(-1)
    else:
        print(dp[N][Y][X])

if __name__ == '__main__':
    main()