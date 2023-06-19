def dfs(state, pos, depth, limit, prev):
    if depth == limit:
        return state == goal
    if depth + h(state) > limit:
        return False
    for d in range(4):
        if prev == d:
            continue
        t = move(state, pos, d)
        if dfs(t[0], t[1], depth + 1, limit, d):
            return True
    return False
