def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[float('inf') for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k] == float('inf'):
                    continue
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                a, b = ab[i]
                dp[i+1][min(j+a, x)][min(k+b, y)] = min(dp[i+1][min(j+a, x)][min(k+b, y)], dp[i][j][k]+1)
    print(dp[n][x][y] if dp[n][x][y] != float('inf') else -1)

if __name__ == '__main__':
    main()