def solve():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 18
    for _ in range(2):
        dp = [[10 ** 18] * (w + 1) for _ in range(h + 1)]
        for i in range(h):
            for j in range(w):
                dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + c
                ans = min(ans, dp[i + 1][j + 1] + a[i][j])
        a = [a[i][::-1] for i in range(h - 1, -1, -1)]
    print(ans)

if __name__ == '__main__':
    solve()