def dfs(used, pos, cnt):
    if cnt > 16:
        return -1
    if used == 0b11111111:
        return cnt
    res = -1
    for i in range(8):
        if pos == i:
            continue
        if not (used & (1 << i)):
            res = max(res, dfs(used | (1 << i), i, cnt+1))
    return res

if __name__ == '__main__':
    dfs()