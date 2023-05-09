def dfs(v, p, d):
    depth[v] = d
    for u in tree[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)

if __name__ == '__main__':
    dfs()