def main():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a1, b1 = map(int, input().split())
        a.append(a1)
        b.append(b1)
    dp = [[[0 for _ in range(y+1)] for _ in range(x+1)] for _ in range(n+1)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(x+1):
            for k in range(y+1):
                if dp[i][j][k] == 1:
                    dp[i+1][j][k] = 1
                    if j+a[i] <= x and k+b[i] <= y:
                        dp[i+1][j+a[i]][k+b[i]] = 1
    for i in range(n, -1, -1):
        if dp[i][x][y] == 1:
            print(i)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()