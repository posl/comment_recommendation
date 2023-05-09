def dfs(i, n, a, b, c, d):
    if i == n:
        return c ^ d
    ans = 0
    for j in range(i + 1, n):
        if b[i][j] == 0:
            b[i][j] = 1
            ans = max(ans, dfs(i + 1, n, a, b, c ^ a[i][j], d))
            b[i][j] = 0
    return ans
