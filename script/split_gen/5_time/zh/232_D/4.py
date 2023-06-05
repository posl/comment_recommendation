def dfs(x,y):
    if x == h-1 and y == w-1:
        return 1
    if x >= h or y >= w:
        return 0
    if d[x][y] != -1:
        return d[x][y]
    if s[x][y] == '#':
        return 0
    d[x][y] = dfs(x+1,y) + dfs(x,y+1)
    return d[x][y]
h,w = map(int,input().split())
s = [input() for i in range(h)]
d = [[-1]*w for i in range(h)]
print(dfs(0,0))
