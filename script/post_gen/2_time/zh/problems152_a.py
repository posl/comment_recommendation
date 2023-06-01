Synthesizing 10/10 solutions

=======
Suggestion 1

def bfs(start, goal):
    INF =

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    s = [[c for c in input()] for _ in range(h)]
    ans = 0
    for si in s:
        ans += si.count('.')
    print(ans - 1)

=======
Suggestion 3

def main():
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans += 1
    if ans == H * W:
        print(-1)
    else:
        print(ans)

=======
Suggestion 4

def dfs(x, y, cnt):
    global ans
    if cnt > ans:
        ans = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == '.' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1)
            visited[nx][ny] = 0

h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
visited = [[0 for _ in range(w)] for _ in range(h)]
ans = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            visited[i][j] = 1
            dfs(i, j, 0)
            visited[i][j] = 0
print(ans)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                ans += 1
    print(ans - 1)

=======
Suggestion 6

def dfs(i,j):
    global maxv
    if i<0 or h<=i or j<0 or w<=j or maze[i][j]=='#':
        return
    if maxv < dist[i][j]:
        maxv = dist[i][j]
    if dist[i][j] != 0:
        return
    dist[i][j] = dist[i][j] + 1
    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j+1)
    dfs(i,j-1)
    dist[i][j] = dist[i][j] - 1
    return

h,w = map(int,input().split())
maze = [list(input()) for i in range(h)]
dist = [[0 for i in range(w)] for i in range(h)]
maxv = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            dfs(i,j)
print(maxv)

=======
Suggestion 7

def bfs(sx, sy):
    dist = [[-1] * w for _ in range(h)]
    dist[sx][sy] = 0
    que = []
    que.append((sx, sy))

    while que:
        x, y = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] != '#' and dist[nx][ny] == -1:
                que.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

    res = 0
    for i in range(h):
        for j in range(w):
            if maze[i][j] != '#' and dist[i][j] != -1:
                res = max(res, dist[i][j])

    return res


h, w = map(int, input().split())
maze = [input() for _ in range(h)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

ans = 0
for sx in range(h):
    for sy in range(w):
        if maze[sx][sy] == '#':
            continue
        ans = max(ans, bfs(sx, sy))

print(ans)

=======
Suggestion 8

def dfs(i,j):
    global maxv
    if i<0 or i>=h or j<0 or j>=w or maze[i][j] == '#':
        return
    if maxv < dist[i][j]:
        maxv = dist[i][j]
    if dist[i][j] != -1:
        return
    dist[i][j] = dist[i][j]+1
    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j+1)
    dfs(i,j-1)
    dist[i][j] = dist[i][j]-1

h,w = map(int,input().split())
maze = [list(input()) for i in range(h)]
dist = [[-1]*w for i in range(h)]
maxv = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            dfs(i,j)
print(maxv)

=======
Suggestion 9

def dfs(x,y):
    if x<0 or x>=h or y<0 or y>=w or maze[x][y]=="#":
        return
    maze[x][y]="#"
    for i in range(4):
        dfs(x+dx[i],y+dy[i])

h,w=map(int,input().split())
maze=[list(input()) for i in range(h)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
ans=0

for i in range(h):
    for j in range(w):
        if maze[i][j]==".":
            dfs(i,j)
            ans+=1

print(ans-1)

=======
Suggestion 10

def dfs(x,y):
    global ans
    ans = max(ans, dist[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and s[nx][ny] != '#' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            dfs(nx,ny)
            dist[nx][ny] = -1

h,w = map(int,input().split())
s = [list(input()) for i in range(h)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        dist = [[-1] * w for i in range(h)]
        dist[i][j] = 0
        dfs(i,j)
print(ans)
