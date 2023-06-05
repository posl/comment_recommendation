def dfs(h, w, k, i, j, k2, w2, h2):
    if i == h:
        if k2 == k:
            return 1
        else:
            return 0
    if j == w:
        return dfs(h, w, k, i + 1, 0, k2, w2, h2)
    if k2 + w2[i] + h2[j] > k:
        return dfs(h, w, k, i, j + 1, k2, w2, h2)
    return dfs(h, w, k, i, j + 1, k2, w2, h2) + dfs(h, w, k, i + 1, j, k2 + 1, w2, h2)
