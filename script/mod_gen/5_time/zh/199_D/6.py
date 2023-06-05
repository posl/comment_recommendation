def dfs(n, m, e, v, i):
    if i == n:
        return 1
    res = 0
    for c in range(3):
        ok = True
        for j in range(i):
            if e[i][j] == 1 and v[j] == c:
                ok = False
                break
        if ok:
            v[i] = c
            res += dfs(n, m, e, v, i + 1)
            v[i] = -1
    return res

if __name__ == '__main__':
    dfs()