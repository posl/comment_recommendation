def dfs(v, p, d):
    if v == p:
        return d
    if d == 4:
        return 0
    for i in range(4):
        if v + dx[i] < 0 or v + dx[i] > 8 or v + dy[i] < 0 or v + dy[i] > 8:
            continue
        if v + dx[i] == p or v + dy[i] == p:
            continue
        if v + dx[i] == 2 and v + dy[i] == 3:
            continue
        if v + dx[i] == 3 and v + dy[i] == 2:
            continue
        if v + dx[i] == 5 and v + dy[i] == 6:
            continue
        if v + dx[i] == 6 and v + dy[i] == 5:
            continue
        if v + dx[i] == 7 and v + dy[i] == 8:
            continue
        if v + dx[i] == 8 and v + dy[i] == 7:
            continue
        if v + dx[i] == 2 and v + dy[i] == 9:
            continue
        if v + dx[i] == 9 and v + dy[i] == 2:
            continue
        if v + dx[i] == 4 and v + dy[i] == 9:
            continue
        if v + dx[i] == 9 and v + dy[i] == 4:
            continue
        if v + dx[i] == 5 and v + dy[i] == 9:
            continue
        if v + dx[i] == 9 and v + dy[i] == 5:
            continue
        if v + dx[i] == 6 and v + dy[i] == 9:
            continue
        if v + dx[i] == 9 and v + dy[i] == 6:
            continue
        if v + dx[i] == 7 and v + dy[i] == 9:
            continue
        if v + dx[i] == 9 and v + dy[i] == 7:
            continue
        if v + dx[i] == 8 and v + dy[i] == 9:
            continue
        if v + dx[i] == 9

if __name__ == '__main__':
    dfs()