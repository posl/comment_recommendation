def main():
    n = int(input())
    x, y = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n)]
    dp = [[[False for k in range(y + 1)] for j in range(x + 1)] for i in range(n + 1)]
    dp[0][0][0] = True
    for i in range(n):
        for j in range(x + 1):
            for k in range(y + 1):
                if dp[i][j][k]:
                    dp[i + 1][j][k] = True
                    if j + ab[i][0] <= x and k + ab[i][1] <= y:
                        dp[i + 1][j + ab[i][0]][k + ab[i][1]] = True
    ans = -1
    for i in range(n + 1):
        if dp[i][x][y]:
            ans = i
            break
    print(ans)

if __name__ == '__main__':
    main()