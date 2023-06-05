def dfs(i, n, a, x, y):
    if i == n:
        return 0
    ans = 0
    for j in range(a[i]):
        if y[i][j] == 1:
            ans = max(ans, dfs(i+1, n, a, x, y) + 1)
        else:
            ans = max(ans, dfs(i+1, n, a, x, y))
    return ans

if __name__ == '__main__':
    dfs()