def dfs(i, j, a, b):
    if i == h:
        return 1
    if j == w:
        return dfs(i+1, 0, a, b)
    if a:
        # 2x1の畳を敷く
        res = dfs(i, j+1, a-1, b)
        # 2x1の畳を縦に敷く
        if i+1 < h and a:
            res += dfs(i, j+1, a-1, b)
    if b:
        # 1x1の畳を敷く
        res += dfs(i, j+1, a, b-1)
    return res
h, w, a, b = map(int, input().split())
print(dfs(0, 0, a, b))

if __name__ == '__main__':
    dfs()