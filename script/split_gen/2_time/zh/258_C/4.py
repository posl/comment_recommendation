def dfs(i, j, k, n, a, used):
    if k == n:
        return 0
    res = 0
    used[i][j] = True
    res = max(res, dfs(i - 1, j, k + 1, n, a, used) * 10 + a[i][j])
    res = max(res, dfs(i + 1, j, k + 1, n, a, used) * 10 + a[i][j])
    res = max(res, dfs(i, j - 1, k + 1, n, a, used) * 10 + a[i][j])
    res = max(res, dfs(i, j + 1, k + 1, n, a, used) * 10 + a[i][j])
    used[i][j] = False
    return res
n = int(input())
a = [list(map(int, input())) for _ in range(n)]
used = [[False] * n for _ in range(n)]
res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j, 0, n, a, used))
print(res)
