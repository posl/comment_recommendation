def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1
    for i in range(h):
        for j in range(w):
            if a[i][j] == "#":
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    print(dp[h - 1][w - 1])
