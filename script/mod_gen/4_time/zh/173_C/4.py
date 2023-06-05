def dfs(i, j, k, h, w, c):
    if i == h:
        return k == 0
    if j == w:
        return dfs(i + 1, 0, k, h, w, c)
    if c[i][j] == '#':
        return dfs(i, j + 1, k - 1, h, w, c)
    return dfs(i, j + 1, k, h, w, c) + dfs(i, j + 1, k - 1, h, w, c)

if __name__ == '__main__':
    dfs()