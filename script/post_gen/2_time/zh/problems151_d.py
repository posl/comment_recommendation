Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_step(h,w,grid):
    max_step = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                max_step = max(max_step, bfs(i,j,h,w,grid))
    return max_step

=======
Suggestion 2

def dfs(h,w,board,cnt):
    global ans
    ans = max(ans,cnt)
    for i in range(h):
        for j in range(w):
            if board[i][j] == '.':
                board[i][j] = '#'
                if i > 0 and board[i-1][j] == '.':
                    dfs(h,w,board,cnt+1)
                if i < h-1 and board[i+1][j] == '.':
                    dfs(h,w,board,cnt+1)
                if j > 0 and board[i][j-1] == '.':
                    dfs(h,w,board,cnt+1)
                if j < w-1 and board[i][j+1] == '.':
                    dfs(h,w,board,cnt+1)
                board[i][j] = '.'

=======
Suggestion 3

def dfs(x, y, dist):
    global max_dist
    max_dist = max(max_dist, dist)
    for dx, dy in dxdy:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if maze[nx][ny] == '#':
            continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, dist + 1)
        visited[nx][ny] = False

H, W = map(int, input().split())
maze = [input() for _ in range(H)]
dxdy = ((0, 1), (1, 0), (0, -1), (-1, 0))
max_dist = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            continue
        visited = [[False]*W for _ in range(H)]
        visited[i][j] = True
        dfs(i, j, 0)
print(max_dist)

=======
Suggestion 4

def main():
    h,w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    #print(s)
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                #print(i,j)
                t = [[-1]*w for _ in range(h)]
                t[i][j] = 0
                q = [(i,j)]
                while q:
                    x,y = q.pop(0)
                    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                        nx,ny = x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and s[nx][ny]=='.' and t[nx][ny]==-1:
                            t[nx][ny] = t[x][y] + 1
                            q.append((nx,ny))
                ans = max(ans, max([max(i) for i in t]))
    print(ans)

=======
Suggestion 5

def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 从每个点出发，求到其他所有点的最短距离
    INF = 1000000007
    d = [[INF] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            d[i][j] = 0
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.' and d[nx][ny] == INF:
                        d[nx][ny] = d[x][y] + 1
                        q.append((nx, ny))
    res = 0
    for i in range(H):
        for j in range(W):
            if d[i][j] == INF:
                continue
            res = max(res, d[i][j])
    return res

print(solve())

=======
Suggestion 6

def read_data():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    return H, W, S

=======
Suggestion 7

def dfs(x,y):
    global ans
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w and s[nx][ny]=='.' and not check[nx][ny]:
            check[nx][ny]=True
            dfs(nx,ny)
            check[nx][ny]=False
            ans=max(ans,check.count(True))

h,w=map(int,input().split())
s=[input() for _ in range(h)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]=='.':
            check=[[False]*w for _ in range(h)]
            check[i][j]=True
            dfs(i,j)
print(ans)

=======
Suggestion 8

def dfs(x,y):
    global max_length
    #print("x,y",x,y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #print("nx,ny",nx,ny)
        if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] == "." and not seen[nx][ny]:
            seen[nx][ny] = True
            dfs(nx,ny)
            seen[nx][ny] = False
        else:
            max_length = max(max_length, sum(sum(seen,[])))

H,W = map(int,input().split())
maze = [list(input()) for _ in range(H)]
seen = [[False]*W for _ in range(H)]
max_length = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(H):
    for j in range(W):
        if maze[i][j] == ".":
            seen[i][j] = True
            dfs(i,j)
            seen[i][j] = False
print(max_length)

=======
Suggestion 9

def dfs(x, y):
    global ans
    ans = max(ans, dist[x][y])
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < h and 0 <= ny < w): continue
        if a[nx][ny] == "#": continue
        if dist[nx][ny] != -1: continue
        dist[nx][ny] = dist[x][y] + 1
        dfs(nx, ny)
        dist[nx][ny] = -1

h, w = map(int, input().split())
a = [input() for _ in range(h)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == "#": continue
        dist = [[-1] * w for _ in range(h)]
        dist[i][j] = 0
        dfs(i, j)
print(ans)

=======
Suggestion 10

def main():
    print("请输入H W")
    H,W = map(int,input().split())
    print("请输入迷宫")
    s = []
    for i in range(H):
        s.append(input())
    print(s)
    #print(s[0][0])
    #print(s[1][1])
    #print(s[2][2])
    #print(s[2][3])
    #print(s[2][4])
    #print(s[1][4])
    #print(s[0][4])
    #print(s[0][3])
    #print(s[0][2])
    print(s[0][0])
    print(s[0][1])
    print(s[0][2])
    print(s[1][2])
    print(s[2][2])
    print(s[2][1])
    print(s[2][0])
    print(s[1][0])
    print(s[1][1])
