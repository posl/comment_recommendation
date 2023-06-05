def dfs(path, n, k, t, visited, cur, ans):
    if len(path) == n:
        if k == t[path[-1]][0]:
            ans[0] += 1
        return
    for i in range(1, n):
        if visited[i] == 0:
            visited[i] = 1
            path.append(i)
            dfs(path, n, k, t, visited, i, ans)
            path.pop()
            visited[i] = 0
