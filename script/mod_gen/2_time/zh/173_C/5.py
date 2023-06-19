def dfs(h, w, k, c):
    if h == 0 and w == 0:
        return 1 if k == 0 else 0
    if h == 0:
        return dfs(w, 0, k, c)
    if w == 0:
        return dfs(h, 0, k, c)
    if k < 0:
        return 0
    if (h, w, k) in c:
        return c[(h, w, k)]
    res = 0
    for i in range(1 << (h + w)):
        cnt = 0
        for j in range(h):
            if (i >> j) & 1:
                cnt += 1
        for j in range(w):
            if (i >> (j + h)) & 1:
                cnt += 1
        for j in range(h):
            for l in range(w):
                if ((i >> j) & 1) and ((i >> (l + h)) & 1):
                    if c[j][l] == '#':
                        cnt -= 1
        if cnt == k:
            res += 1
    c[(h, w, k)] = res
    return res
h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
print(dfs(h, w, k, {}))
