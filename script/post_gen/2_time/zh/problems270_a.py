Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(x, y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000:
        return
    if c[x][y]:
        return
    c[x][y] = True
    dfs(x - 1, y - 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x + 1, y)
    dfs(x + 1, y + 1)

n = int(input())
c = [[False for i in range(2000)] for j in range(2000)]
for i in range(n):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    c[x][y] = True
ans = 0
for i in range(2000):
    for j in range(2000):
        if c[i][j]:
            dfs(i, j)
            ans += 1
print(ans)

=======
Suggestion 2

def dfs(x, y):
    if x < 0 or x >= 1000 or y < 0 or y >= 1000:
        return
    if graph[x][y] == 0:
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
graph = [[0 for _ in range(1000)] for _ in range(1000)]
visited = [[False for _ in range(1000)] for _ in range(1000)]
for i in range(n):
    x, y = map(int, input().split())
    graph[x + 500][y + 500] = 1
ans = 0
for i in range(1000):
    for j in range(1000):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            ans += 1
print(ans)

=======
Suggestion 3

def dfs(i,j):
    if i < 0 or i >= 2000 or j < 0 or j >= 2000:
        return
    if color[i][j] == 0:
        return
    if visited[i][j]:
        return
    visited[i][j] = True
    dfs(i-1,j-1)
    dfs(i-1,j)
    dfs(i,j-1)
    dfs(i,j+1)
    dfs(i+1,j)
    dfs(i+1,j+1)

n = int(input())
color = [[0]*2000 for i in range(2000)]
visited = [[False]*2000 for i in range(2000)]
for i in range(n):
    x,y = map(int,input().split())
    x += 1000
    y += 1000
    color[x][y] = 1
ans = 0
for i in range(2000):
    for j in range(2000):
        if color[i][j] == 1 and not visited[i][j]:
            dfs(i,j)
            ans += 1
print(ans)

=======
Suggestion 4

def dfs(x, y):
    if x < 0 or x >= 2001 or y < 0 or y >= 2001:
        return
    if visited[x][y]:
        return
    if not grid[x][y]:
        return
    visited[x][y] = True
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx, ny)


dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]
grid = [[False] * 2001 for _ in range(2001)]
visited = [[False] * 2001 for _ in range(2001)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    grid[x][y] = True

ans = 0
for i in range(2001):
    for j in range(2001):
        if not visited[i][j] and grid[i][j]:
            dfs(i, j)
            ans += 1
print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)

    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            dx = x[i] - x[j]
            dy = y[i] - y[j]
            if dx*dx + dy*dy == 3:
                ans += 1

    print(ans)

=======
Suggestion 6

def dfs(x,y):
    if x<0 or x>1000 or y<0 or y>1000 or (x,y) in used or (x,y) not in black:
        return
    used.add((x,y))
    for i in range(-1,2):
        for j in range(-1,2):
            if i!=j:
                dfs(x+i,y+j)

n=int(input())
black=set()
for i in range(n):
    x,y=map(int,input().split())
    black.add((x,y))
used=set()
ans=0
for x,y in black:
    if (x,y) not in used:
        ans+=1
        dfs(x,y)
print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    #print(X)
    #print(Y)
    #print(len(X))
    #print(len(Y))
    #print(X[0])
    #print(Y[0])
    #print(X[0] - Y[0])
    #print(X[0] + Y[0])
    #print(X[1] - Y[1])
    #print(X[1] + Y[1])
    #print(X[2] - Y[2])
    #print(X[2] + Y[2])
    #print(X[3] - Y[3])
    #print(X[3] + Y[3])
    #print(X[4] - Y[4])
    #print(X[4] + Y[4])
    #print(X[5] - Y[5])
    #print(X[5] + Y[5])
    #print(X[6] - Y[6])
    #print(X[6] + Y[6])
    #print(X[7] - Y[7])
    #print(X[7] + Y[7])
    #print(X[8] - Y[8])
    #print(X[8] + Y[8])
    #print(X[9] - Y[9])
    #print(X[9] + Y[9])
    #print(X[10] - Y[10])
    #print(X[10] + Y[10])
    #print(X[11] - Y[11])
    #print(X[11] + Y[11])
    #print(X[12] - Y[12])
    #print(X[12] + Y[12])
    #print(X[13] - Y[13])
    #print(X[13] + Y[13])
    #print(X[14] - Y[14])
    #print(X[14] + Y[14])
    #print(X[15] - Y[15])
    #print(X[15] + Y[15])
    #print(X[16] - Y[16])
    #print(X[16] + Y[16])
    #print(X[17] - Y[17])

=======
Suggestion 8

def dfs(i,j):
    if i<0 or j<0 or i>=1000 or j>=1000:
        return
    if visit[i][j] == 1:
        return
    if grid[i][j] == 0:
        return
    visit[i][j] = 1
    dfs(i-1,j-1)
    dfs(i-1,j)
    dfs(i,j-1)
    dfs(i,j+1)
    dfs(i+1,j)
    dfs(i+1,j+1)

N = int(input())
grid = [[0 for i in range(1000)] for j in range(1000)]
visit = [[0 for i in range(1000)] for j in range(1000)]
for i in range(N):
    x,y = input().split()
    x = int(x)+500
    y = int(y)+500
    grid[x][y] = 1
ans = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] == 1 and visit[i][j] == 0:
            dfs(i,j)
            ans += 1
print(ans)

=======
Suggestion 9

def main():
    # 读入数据
    N = int(input())
    # 建立一个字典，记录黑色格子的坐标
    black = {}
    for i in range(N):
        x, y = map(int, input().split())
        black[(x, y)] = True
    # 定义六个方向
    dx = [-1, -1, 0, 0, 1, 1]
    dy = [-1, 0, -1, 1, 0, 1]
    # 定义一个集合，记录已经访问过的格子
    visited = {}
    # 定义一个函数，用于深度优先搜索
    def dfs(x, y):
        # 如果已经访问过了，则返回
        if visited.get((x, y)):
            return
        # 访问格子(x, y)
        visited[(x, y)] = True
        # 深度优先搜索
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            # 如果是白色格子，则返回
            if not black.get((nx, ny)):
                continue
            # 递归地访问相邻的格子
            dfs(nx, ny)
    # 计算答案
    ans = 0
    for x, y in black.keys():
        # 如果已经访问过，则返回
        if visited.get((x, y)):
            continue
        # 如果是白色格子，则返回
        if not black.get((x, y)):
            continue
        # 递归地访问相邻的格子
        dfs(x, y)
        # 计算答案
        ans += 1
    # 输出答案
    print(ans)

=======
Suggestion 10

def dfs(x,y):
    if x<0 or x>=2000 or y<0 or y>=2000:
        return
    if m[x][y]==0:
        return
    if visited[x][y]:
        return
    visited[x][y]=True
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

n=int(input())
m=[[0]*2000 for _ in range(2000)]
visited=[[False]*2000 for _ in range(2000)]
for _ in range(n):
    x,y=map(int,input().split())
    m[x+1000][y+1000]=1
ans=0
for i in range(2000):
    for j in range(2000):
        if visited[i][j]==False and m[i][j]==1:
            dfs(i,j)
            ans+=1
print(ans)
