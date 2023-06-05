def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 18
    for _ in range(2):
        dp = [[10 ** 18] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                ans = min(ans, a[i][j] + c * (i + j) + dp[i][j])
        a = [row[::-1] for row in a]
    print(ans)

if __name__ == '__main__':
    main()