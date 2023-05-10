def dfs(G, v, p, d, D):
    D[v] = d
    for w in G[v]:
        if w != p:
            dfs(G, w, v, d + 1, D)

if __name__ == '__main__':
    dfs()