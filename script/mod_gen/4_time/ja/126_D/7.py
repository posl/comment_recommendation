def dfs(G, v, p, d):
    color[v] = d
    for next_v in G[v]:
        if next_v == p:
            continue
        dfs(G, next_v, v, d ^ 1)

if __name__ == '__main__':
    dfs()