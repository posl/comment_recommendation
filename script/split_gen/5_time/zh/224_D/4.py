def dfs(puz,depth):
    if depth > 16:
        return -1
    if puz == end:
        return depth
    if puz in visited:
        return -1
    visited.append(puz)
    for i in range(9):
        if puz[i] == 0:
            break
    for j in range(9):
        if j == i or puz[j] == 0:
            continue
        puz[i],puz[j] = puz[j],puz[i]
        if puz not in visited:
            res = dfs(puz,depth+1)
            if res != -1:
                return res
        puz[i],puz[j] = puz[j],puz[i]
    return -1
start = [1,2,3,4,5,6,7,8,0]
end = list(map(int,input().split()))
visited = []
print(dfs(end,0))
