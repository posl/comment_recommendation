def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[False for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = True
    for i in range(n):
        a, b = ab[i]
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k]:
                    dp[i+1][j][k] = True
                    if j+a <= x and k+b <= y:
                        dp[i+1][j+a][k+b] = True
    for i in range(n, -1, -1):
        if dp[i][x][y]:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()