def dfs(u, p):
    for v, w in g[u]:
        if v == p:
            continue
        d[v] = d[u] + w
        dfs(v, u)

if __name__ == '__main__':
    dfs()