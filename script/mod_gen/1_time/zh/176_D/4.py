def dfs(i, j, k):
    if i == dh and j == dw:
        return k
    if k >= 3:
        return -1
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    res = 10**9
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '.':
            res = min(res, dfs(ni, nj, k))
        else:
            for di2, dj2 in d:
                ni2, nj2 = ni + di2, nj + dj2
                if 0 <= ni2 < h and 0 <= nj2 < w and s[ni2][nj2] == '.':
                    res = min(res, dfs(ni2, nj2, k + 1))
    dp[i][j][k] = res
    return res
h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch, cw, dh, dw = ch - 1, cw - 1, dh - 1, dw - 1
s = [input() for _ in range(h)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
dp = [[[-1] * 4 for _ in range(w)] for _ in range(h)]
print(dfs(ch, cw, 0))
