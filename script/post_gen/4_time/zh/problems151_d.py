Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_step(h, w, s):
    max_step = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                max_step = max(max_step, get_max_step_from_point(h, w, s, i, j))
    return max_step

=======
Suggestion 2

def dfs(h, w, s, i, j, v):
    s[i][j] = '#'
    v += 1
    if i > 0 and s[i-1][j] == '.':
        v = dfs(h, w, s, i-1, j, v)
    if i < h-1 and s[i+1][j] == '.':
        v = dfs(h, w, s, i+1, j, v)
    if j > 0 and s[i][j-1] == '.':
        v = dfs(h, w, s, i, j-1, v)
    if j < w-1 and s[i][j+1] == '.':
        v = dfs(h, w, s, i, j+1, v)
    s[i][j] = '.'
    return v

=======
Suggestion 3

def dfs(i,j):
    global ans
    ans = max(ans,cnt[i][j])
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '.' and cnt[ni][nj] == 0:
            cnt[ni][nj] = cnt[i][j] + 1
            dfs(ni,nj)
            cnt[ni][nj] = 0

h,w = map(int,input().split())
s = [input() for _ in range(h)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            cnt = [[0]*w for _ in range(h)]
            cnt[i][j] = 1
            dfs(i,j)
print(ans-1)

=======
Suggestion 4

def main():
    # H,W = map(int,input().split())
    H,W = 3,5
    # S = [input() for i in range(H)]
    S = ['...#.','.#.#.','.#...']
    # print(H,W,S)
    print(S[0])
    print(S[1])
    print(S[2])

    # print(H,W,S)
    print(S[0])
    print(S[1])
    print(S[2])

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                ans += 1
    print(ans - 1)

=======
Suggestion 6

def dfs(x,y):
    global ans
    ans = max(ans, dist[x][y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and c[nx][ny] == '.' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            dfs(nx, ny)
            dist[nx][ny] = -1

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]
dist = [[-1]*w for _ in range(h)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ans = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == '.':
            dist = [[-1]*w for _ in range(h)]
            dist[i][j] = 0
            dfs(i,j)

print(ans)

=======
Suggestion 7

def bfs(sx, sy):
    dist = [[-1] * w for _ in range(h)]
    dist[sx][sy] = 0
    que = []
    que.append(sx)
    que.append(sy)
    while len(que) > 0:
        x = que.pop(0)
        y = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < h and 0 <= ny and ny < w and maze[nx][ny] != "#" and dist[nx][ny] == -1:
                que.append(nx)
                que.append(ny)
                dist[nx][ny] = dist[x][y] + 1
    res = 0
    for i in range(h):
        for j in range(w):
            if maze[i][j] != "#" and dist[i][j] != -1:
                res = max(res, dist[i][j])
    return res

h, w = map(int, input().split())
maze = [list(input()) for _ in range(h)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0
for sx in range(h):
    for sy in range(w):
        if maze[sx][sy] == ".":
            ans = max(ans, bfs(sx, sy))
print(ans)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans = max(ans, dfs(h, w, S))
    print(ans)

=======
Suggestion 9

def dfs(i,j):
    global ans
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue
        if maze[ni][nj] == "#":
            continue
        if seen[ni][nj] == True:
            continue
        seen[ni][nj] = True
        dfs(ni,nj)
        seen[ni][nj] = False
    ans = max(ans,sum(seen,[]))

h,w = map(int,input().split())
maze = [list(input()) for _ in range(h)]
seen = [[False]*w for _ in range(h)]
ans = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(h):
    for j in range(w):
        if maze[i][j] == "#":
            continue
        seen[i][j] = True
        dfs(i,j)
        seen[i][j] = False
print(ans-1)

=======
Suggestion 10

def dfs(x,y,step):
    global max_step
    if x==H-1 and y==W-1:
        if max_step<step:
            max_step=step
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<H and 0<=ny<W and S[nx][ny]=="." and visited[nx][ny]==False:
            visited[nx][ny]=True
            dfs(nx,ny,step+1)
            visited[nx][ny]=False

H,W=map(int,input().split())
S=[list(input()) for _ in range(H)]
visited=[[False]*W for _ in range(H)]
max_step=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
visited[0][0]=True
dfs(0,0,1)
print(max_step)
