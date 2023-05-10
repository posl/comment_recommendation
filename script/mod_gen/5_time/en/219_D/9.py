def main():
    n = int(input())
    x, y = map(int, input().split())
    lunchboxes = [tuple(map(int, input().split())) for _ in range(n)]
    dp = [[False] * (y+1) for _ in range(x+1)]
    dp[0][0] = True
    for a, b in lunchboxes:
        for i in range(x, -1, -1):
            for j in range(y, -1, -1):
                if dp[i][j] and i+a <= x and j+b <= y:
                    dp[i+a][j+b] = True
    for i in range(x+1):
        for j in range(y+1):
            if dp[x-i][y-j]:
                print(x-i+y-j)
                return
    print(-1)

if __name__ == '__main__':
    main()