def dfs(v, p, d):
    global dist
    global parent
    global depth
    parent[v] = p
    depth[v] = d
    dist[v] = d
    for u in graph[v]:
        if u == p:
            continue
        dfs(u, v, d + 1)
        dist[v] = min(dist[v], dist[u])

if __name__ == '__main__':
    dfs()