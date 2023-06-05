def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 18
    for _ in range(2):
        dp = [[10 ** 18] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                for di, dj in ((-1, 0), (0, -1)):
                    if i + di >= 0 and j + dj >= 0:
                        dp[i][j] = min(dp[i][j], dp[i + di][j + dj])
                dp[i][j] = min(dp[i][j], a[i][j] + c * i + c * j)
                ans = min(ans, dp[i][j] + a[i][j] + c * i + c * j)
        a = a[::-1]
    print(ans)

if __name__ == '__main__':
    main()