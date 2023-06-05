def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 18
    for _ in range(2):
        dp = [[10 ** 18] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                for di, dj in ((0, 1), (1, 0)):
                    ni, nj = i + di, j + dj
                    if ni < h and nj < w:
                        dp[ni][nj] = min(dp[ni][nj], dp[i][j] + c)
                dp[i][j] = min(dp[i][j], a[i][j])
                ans = min(ans, dp[i][j] + a[i][j] + c)
        a = [row[::-1] for row in a]
    print(ans)
