def dfs(n, m, p):
    if n == 9:
        if m == 0:
            return 0
        else:
            return -1
    if m == 0:
        return -1
    if p[n] == n:
        return dfs(n + 1, m, p)
    res = -1
    for i in range(n + 1, 9):
        if p[i] == n:
            p[i] = p[n]
            tmp = dfs(n + 1, m - 1, p)
            p[i] = i
            if tmp != -1:
                if res == -1:
                    res = tmp + 1
                else:
                    res = min(res, tmp + 1)
    return res

if __name__ == '__main__':
    dfs()