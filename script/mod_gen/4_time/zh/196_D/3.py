def dfs(i, j, a, b, h, w):
    #print(i, j, a, b)
    if i == h:
        return dfs(0, j + 1, a, b, h, w)
    if j == w:
        return 1
    if a == 0 and b == 0:
        return 0
    if j == w - 1:
        return dfs(i + 1, j, a - 1, b, h, w)
    else:
        return dfs(i + 1, j, a - 1, b, h, w) + dfs(i, j + 2, a, b - 1, h, w)

if __name__ == '__main__':
    dfs()