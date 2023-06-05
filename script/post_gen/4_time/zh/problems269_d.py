Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(x,y):
    if not (x,y) in s:
        return
    s.remove((x,y))
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

n = int(input())
s = set()
for i in range(n):
    x,y = map(int,input().split())
    s.add((x,y))
ans = 0
while len(s)>0:
    x,y = s.pop()
    dfs(x,y)
    ans += 1
print(ans)

=======
Suggestion 2

def dfs(x, y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000:
        return
    if grid[x][y] == 0:
        return
    if visited[x][y]:
        return
    visited[x][y] = True
    dfs(x - 1, y - 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x + 1, y)
    dfs(x + 1, y + 1)

n = int(input())
grid = [[0] * 2000 for _ in range(2000)]
visited = [[False] * 2000 for _ in range(2000)]

for _ in range(n):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    grid[x][y] = 1

result = 0
for i in range(2000):
    for j in range(2000):
        if grid[i][j] == 0:
            continue
        if visited[i][j]:
            continue
        dfs(i, j)
        result += 1

print(result)

=======
Suggestion 3

def get_adjacent_list(x,y):
    adjacent_list = []
    adjacent_list.append((x-1,y-1))
    adjacent_list.append((x-1,y))
    adjacent_list.append((x,y-1))
    adjacent_list.append((x,y+1))
    adjacent_list.append((x+1,y))
    adjacent_list.append((x+1,y+1))
    return adjacent_list

=======
Suggestion 4

def dfs(x, y):
    global dx, dy, N, grid
    grid[x][y] = 0
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
            dfs(nx, ny)

N = int(input())
grid = [[0] * 2000 for _ in range(2000)]
dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]
for i in range(N):
    x, y = map(int, input().split())
    x += 500
    y += 500
    grid[x][y] = 1

ans = 0
for i in range(2000):
    for j in range(2000):
        if grid[i][j] == 1:
            dfs(i, j)
            ans += 1
print(ans)

=======
Suggestion 5

def dfs(i, j, visited, grid, n):
    visited[i][j] = True
    for k in range(6):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1 and not visited[ni][nj]:
            dfs(ni, nj, visited, grid, n)


n = int(input())
grid = [[0 for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]
for _ in range(n):
    x, y = map(int, input().split())
    grid[x + n - 1][y + n - 1] = 1

di = [-1, -1, 0, 0, 1, 1]
dj = [-1, 0, -1, 1, 0, 1]
visited = [[False for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]

ans = 0
for i in range(2 * n - 1):
    for j in range(2 * n - 1):
        if grid[i][j] == 1 and not visited[i][j]:
            dfs(i, j, visited, grid, 2 * n - 1)
            ans += 1

print(ans)

=======
Suggestion 6

def dfs(x,y):
    if x<0 or x>=1000 or y<0 or y>=1000:
        return
    if not f[x][y]:
        return
    f[x][y]=0
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

n=int(input())
f=[[0]*1000 for i in range(1000)]
for i in range(n):
    x,y=map(int,input().split())
    x+=500
    y+=500
    f[x][y]=1
ans=0
for i in range(1000):
    for j in range(1000):
        if f[i][j]:
            ans+=1
            dfs(i,j)
print(ans)

=======
Suggestion 7

def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=n:
        return
    if a[x][y] == 0:
        return
    a[x][y] = 0
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
    dfs(x-1,y-1)

n = int(input())
a = [[0]*n for _ in range(n)]
for _ in range(n):
    x,y = map(int,input().split())
    a[x][y] = 1

ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            dfs(i,j)
            ans += 1
print(ans)

=======
Suggestion 8

def dfs(v):
    seen[v]=True
    for i in range(len(G[v])):
        if seen[G[v][i]]==False:
            dfs(G[v][i])
            
N=int(input())
X=[0]*N
Y=[0]*N
for i in range(N):
    X[i],Y[i]=map(int,input().split())
    
G=[[] for i in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if X[i]-X[j]==1 and Y[i]-Y[j]==0:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==0 and Y[i]-Y[j]==1:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==-1 and Y[i]-Y[j]==1:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==1 and Y[i]-Y[j]==-1:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==0 and Y[i]-Y[j]==-1:
            G[i].append(j)
            G[j].append(i)
        if X[i]-X[j]==-1 and Y[i]-Y[j]==0:
            G[i].append(j)
            G[j].append(i)

seen=[False]*N
ans=0
for i in range(N):
    if seen[i]==False:
        dfs(i)
        ans+=1
print(ans)

=======
Suggestion 9

def dfs(x,y):
    if x<0 or x>=1001 or y<0 or y>=1001:
        return
    if visited[x][y]:
        return
    if not grid[x][y]:
        return
    visited[x][y]=True
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

N=int(input())
grid=[[False]*1001 for _ in range(1001)]
visited=[[False]*1001 for _ in range(1001)]
for _ in range(N):
    x,y=map(int,input().split())
    grid[x][y]=True
ans=0
for i in range(1001):
    for j in range(1001):
        if not visited[i][j] and grid[i][j]:
            dfs(i,j)
            ans+=1
print(ans)

=======
Suggestion 10

def dfs(x,y):
    #print(x,y)
    if (x,y) in black:
        black.remove((x,y))
        dfs(x-1,y-1)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x+1,y+1)

N=int(input())
black=[]
for i in range(N):
    x,y=map(int,input().split())
    black.append((x,y))

ans=0
while black:
    ans+=1
    dfs(black[0][0],black[0][1])

print(ans)
