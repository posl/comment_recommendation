def dfs(i, j):
    if i == h-1 and j == w-1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    res = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < h and 0 <= nj < w:
            if c[ni][nj] == ".":
                res += dfs(ni, nj)
    dp[i][j] = res
    return res
h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
dp = [[-1]*w for _ in range(h)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
print(dfs(0, 0))
