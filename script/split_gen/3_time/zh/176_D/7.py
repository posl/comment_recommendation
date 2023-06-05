def dfs(x,y):
    if x == d_h and y == d_w:
        return 0
    if visited[x][y]:
        return float('inf')
    visited[x][y] = True
    res = float('inf')
    for dx in range(-2,3):
        for dy in range(-2,3):
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.':
                res = min(res,dfs(nx,ny) + 1)
    visited[x][y] = False
    return res
h,w = map(int,input().split())
c_h,c_w = map(int,input().split())
d_h,d_w = map(int,input().split())
c_h -= 1
c_w -= 1
d_h -= 1
d_w -= 1
s = []
for i in range(h):
    s.append(input())
visited = [[False] * w for _ in range(h)]
ans = dfs(c_h,c_w)
