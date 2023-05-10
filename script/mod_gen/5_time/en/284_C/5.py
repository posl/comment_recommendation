def dfs(v, G, seen):
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]: continue
        dfs(next_v, G, seen)

if __name__ == '__main__':
    dfs()