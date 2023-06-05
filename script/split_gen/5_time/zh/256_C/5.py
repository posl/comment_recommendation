def dfs(i, j, h, w):
    if i == 2 and j == 2:
        if h[0] == 0 and h[1] == 0 and h[2] == 0 and w[0] == 0 and w[1] == 0 and w[2] == 0:
            return 1
        else:
            return 0
    if j == 2:
        j = 0
        i += 1
    if h[i] < 0 or w[j] < 0:
        return 0
    res = 0
    for k in range(10):
        h[i] -= k
        w[j] -= k
        res += dfs(i, j + 1, h, w)
        h[i] += k
        w[j] += k
    return res
