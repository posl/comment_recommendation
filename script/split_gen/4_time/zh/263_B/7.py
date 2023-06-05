def solve(n, p):
    def dfs(i):
        if i == 0:
            return 0
        return dfs(p[i-1]) + 1
    return dfs(n)
