def dfs(v, seen, g):
    seen[v] = True
    for next_v in g[v]:
        if seen[next_v]:
            continue
        dfs(next_v, seen, g)

if __name__ == '__main__':
    dfs()