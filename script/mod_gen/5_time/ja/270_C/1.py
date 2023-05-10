def dfs(v, p, g, path):
    path.append(v)
    for nv in g[v]:
        if nv != p:
            dfs(nv, v, g, path)
            path.append(v)

if __name__ == '__main__':
    dfs()