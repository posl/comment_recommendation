def dfs(i, j, n, m, k, c):
    if i == n and j == m:
        if k == 0:
            return 1
        else:
            return 0
    if c[i][j] == '#':
        return dfs(i + 1, j, n, m, k, c)
    else:
        c1 = dfs(i + 1, j, n, m, k - 1, c)
        c2 = dfs(i, j + 1, n, m, k - 1, c)
        return c1 + c2

if __name__ == '__main__':
    dfs()