def dfs(n, cnt):
    if n == 0:
        return cnt
    if n < 0:
        return 10**9
    return min(dfs(n-1, cnt+1), dfs(n-6, cnt+1), dfs(n-9, cnt+1))
