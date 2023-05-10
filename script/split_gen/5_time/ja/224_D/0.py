def dfs(v, p):
    global seen
    global cnt
    global G
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        if next_v == p:
            continue
        cnt += 1
        dfs(next_v, v)
