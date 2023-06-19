def dfs(n, m, a, ans):
    if len(a) == n:
        ans.append(a)
    else:
        for i in range(1, m+1):
            if len(a) == 0 or a[-1] < i:
                dfs(n, m, a+[i], ans)
