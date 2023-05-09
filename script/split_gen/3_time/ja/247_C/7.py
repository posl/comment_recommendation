def dfs(n, s):
    if n == 0:
        return s
    return dfs(n - 1, s + [n] + s)
