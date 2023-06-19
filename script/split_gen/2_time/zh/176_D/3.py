def check(x,y):
    if x < 0 or x >= h:
        return False
    if y < 0 or y >= w:
        return False
    if s[x][y] == '#':
        return False
    return True
h,w = map(int,input().split())
ch,cw = map(int,input().split())
dh,dw = map(int,input().split())
s = [input() for _ in range(h)]
ch -= 1
cw -= 1
dh -= 1
dw -= 1
dist = [[-1]*w for _ in range(h)]
dist[ch][cw] = 0
q = [(ch,cw)]
while q:
    x,y = q.pop(0)
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx = x + dx
        ny = y + dy
        if not check(nx,ny):
            continue
        if dist[nx][ny] != -1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))
for i in range(h):
    for j in range(w):
        if dist[i][j] == -1:
            continue
        dist[i][j] = dist[i][j]//3
