def dfs(v, g, ans):
    for u in g[v]:
        if ans[u] == -1:
            ans[u] = v
            dfs(u, g, ans)

if __name__ == '__main__':
    dfs()