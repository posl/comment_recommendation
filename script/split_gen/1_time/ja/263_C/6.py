def dfs(n, m, s, ans):
    if len(s) == n:
        ans.append(s)
        return
    for i in range(1, m+1):
        if len(s) == 0 or s[-1] < i:
            dfs(n, m, s+[i], ans)
