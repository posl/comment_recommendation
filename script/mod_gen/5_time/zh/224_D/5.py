def dfs(state, depth, prev):
    if depth + state[0] > limit:
        return False
    if state[1:] == goal:
        return True
    min = 100
    for i in range(4):
        if prev == i:
            continue
        next = state[:]
        next[0] += 1
        for j in range(8):
            next[j+1] += dir[i][j]
        if dfs(next, depth + 1, i):
            return True
    return False

if __name__ == '__main__':
    dfs()