def dfs(x, y, k, a, b, c):
    if x == 0:
        if k == 0:
            return 1
        else:
            return 0
    if y == 0:
        return dfs(x - 1, b, k, a, b, c)
    if c[x - 1][y - 1] == "#":
        return dfs(x, y - 1, k - 1, a, b, c) + dfs(x, y - 1, k, a, b, c)
    else:
        return dfs(x, y - 1, k, a, b, c)

if __name__ == '__main__':
    dfs()