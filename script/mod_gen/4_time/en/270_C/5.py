def dfs(v, p, g, d):
    for u in g[v]:
        if u == p:
            continue
        d[u] = d[v] + 1
        dfs(u, v, g, d)

if __name__ == '__main__':
    dfs()