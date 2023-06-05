def search(i, j, l, r, dp, w, v, x):
    if i == l and j == r:
        return 0
    if dp[i][j][l][r] != -1:
        return dp[i][j][l][r]
    res = 0
    if i < l:
        res = max(res, search(i + 1, j, l, r, dp, w, v, x))
    if j > r:
        res = max(res, search(i, j - 1, l, r, dp, w, v, x))
    if i < l and j > r:
        res = max(res, search(i + 1, j - 1, l, r, dp, w, v, x))
    if x[l] < w[i] and x[r] < w[j]:
        res = max(res, search(i + 1, j - 1, l + 1, r - 1, dp, w, v, x) + v[i] + v[j])
    if x[l] < w[i] and x[r] >= w[j]:
        res = max(res, search(i + 1, j, l + 1, r, dp, w, v, x) + v[i])
    if x[l] >= w[i] and x[r] < w[j]:
        res = max(res, search(i, j - 1, l, r - 1, dp, w, v, x) + v[j])
    dp[i][j][l][r] = res
    return res

if __name__ == '__main__':
    search()