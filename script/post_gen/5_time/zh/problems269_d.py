Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

=======
Suggestion 3

def dfs(x,y):
    if not(0<=x<=2000 and 0<=y<=2000):
        return
    if not (x,y) in d:
        return
    if d[(x,y)]:
        return
    d[(x,y)]=True
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

n=int(input())
d={}
for i in range(n):
    x,y=map(int,input().split())
    d[(x,y)]=False
cnt=0
for i in range(n):
    if not d[(x,y)]:
        cnt+=1
        dfs(x,y)
print(cnt)

=======
Suggestion 4

def dfs(i,j):
    if i<0 or i>=1001 or j<0 or j>=1001:
        return
    if visited[i][j] == 1:
        return
    if grid[i][j] == 0:
        return

    visited[i][j] = 1
    dfs(i-1,j-1)
    dfs(i-1,j)
    dfs(i,j-1)
    dfs(i,j+1)
    dfs(i+1,j)
    dfs(i+1,j+1)

    return

N = int(input())
grid = [[0 for i in range(1001)] for j in range(1001)]
visited = [[0 for i in range(1001)] for j in range(1001)]
for i in range(N):
    x,y = map(int,input().split())
    grid[x+500][y+500] = 1

count = 0
for i in range(1001):
    for j in range(1001):
        if visited[i][j] == 0 and grid[i][j] == 1:
            dfs(i,j)
            count += 1

print(count)

=======
Suggestion 5

def dfs(x, y):
    global n, m, a
    a[x][y] = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
                dfs(nx, ny)

n = int(input())
m = 1000
a = [[0] * m for _ in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    x += 500
    y += 500
    a[x][y] = 1
ans = 0
for i in range(m):
    for j in range(m):
        if a[i][j] == 1:
            dfs(i, j)
            ans += 1
print(ans)

=======
Suggestion 6

def dfs(x,y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000:
        return
    if graph[x][y] == 0:
        return
    if visited[x][y]:
        return
    visited[x][y] = True
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

n = int(input())
graph = [[0 for _ in range(2000)] for _ in range(2000)]
visited = [[False for _ in range(2000)] for _ in range(2000)]
for _ in range(n):
    x,y = map(int,input().split())
    x += 1000
    y += 1000
    graph[x][y] = 1
ans = 0
for i in range(2000):
    for j in range(2000):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i,j)
            ans += 1
print(ans)

=======
Suggestion 7

def dfs(x, y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if not (x, y) in d:
        return
    if d[(x, y)]:
        return
    d[(x, y)] = True
    dfs(x - 1, y - 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x + 1, y)
    dfs(x + 1, y + 1)

n = int(input())
d = {}
for i in range(n):
    x, y = map(int, input().split())
    d[(x, y)] = False
ans = 0
for k, v in d.items():
    if not v:
        ans += 1
        dfs(k[0], k[1])
print(ans)

=======
Suggestion 8

def dfs(x,y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if (x,y) in visited:
        return
    visited.add((x,y))
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

N = int(input())
visited = set()
for _ in range(N):
    x,y = map(int,input().split())
    dfs(x,y)
print(len(visited))

=======
Suggestion 9

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        X, Y = map(int, input().split())
        x.append(X)
        y.append(Y)
    print(len(set(zip(x, y))))
