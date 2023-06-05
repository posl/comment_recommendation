def dfs(i, a, b, h, w):
    if i == h*w:
        return 1
    if used[i]:
        return dfs(i+1, a, b, h, w)
    ret = 0
    used[i] = True
    ret += dfs(i+1, a, b, h, w)
    used[i] = False
    if i%w != w-1 and not used[i+1]:
        used[i] = used[i+1] = True
        ret += dfs(i+1, a, b-1, h, w)
        used[i] = used[i+1] = False
    if i+w < h*w and not used[i+w]:
        used[i] = used[i+w] = True
        ret += dfs(i+1, a-1, b, h, w)
        used[i] = used[i+w] = False
    return ret
h, w, a, b = map(int, input().split())
used = [False]*(h*w)
print(dfs(0, a, b, h, w))
