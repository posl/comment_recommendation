def dfs(i, j, a, b):
    if i == h - 1 and j == w:
        return 1
    if j == w:
        j = 0
        i += 1
    if t[i][j]:
        return dfs(i, j + 1, a, b)
    res = 0
    if b:
        t[i][j] = 1
        res += dfs(i, j + 1, a, b - 1)
        t[i][j] = 0
    if a and i < h - 1 and t[i + 1][j] == 0:
        t[i][j] = t[i + 1][j] = 1
        res += dfs(i, j + 1, a - 1, b)
        t[i][j] = t[i + 1][j] = 0
    return res
h, w, a, b = map(int, input().split())
t = [[0] * w for i in range(h)]
print(dfs(0, 0, a, b))
