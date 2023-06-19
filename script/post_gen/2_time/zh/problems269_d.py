Synthesizing 10/10 solutions

=======
Suggestion 1

def get_neighbour(x, y):
    if x % 2 == 0:
        return [(x-1, y-1), (x-1, y), (x, y-1), (x, y+1), (x+1, y), (x+1, y+1)]
    else:
        return [(x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y)]

=======
Suggestion 2

def search(x, y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if (x, y) in black:
        return
    black.add((x, y))
    search(x - 1, y - 1)
    search(x - 1, y)
    search(x, y - 1)
    search(x, y + 1)
    search(x + 1, y)
    search(x + 1, y + 1)

n = int(input())
black = set()
for _ in range(n):
    x, y = map(int, input().split())
    search(x, y)
print(len(black))

=======
Suggestion 3

def dfs(x, y):
    if x < 0 or x >= 2001 or y < 0 or y >= 2001 or field[x][y] == 0:
        return
    field[x][y] = 0
    dfs(x-1, y-1)
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    dfs(x+1, y)
    dfs(x+1, y+1)
    return

n = int(input())
field = [[0]*2001 for i in range(2001)]
for i in range(n):
    x, y = map(int, input().split())
    field[x+1000][y+1000] = 1
ans = 0
for i in range(2001):
    for j in range(2001):
        if field[i][j] == 1:
            dfs(i, j)
            ans += 1
print(ans)

=======
Suggestion 4

def dfs(x, y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if (x, y) not in visited:
        visited.add((x, y))
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)

n = int(input())
visited = set()
for i in range(n):
    x, y = map(int, input().split())
    dfs(x, y)
print(len(visited))

=======
Suggestion 5

def dfs(x, y):
    if (x, y) in black:
        black.remove((x, y))
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)

n = int(input())
black = set()
for i in range(n):
    x, y = map(int, input().split())
    black.add((x, y))
ans = 0
while black:
    x, y = black.pop()
    ans += 1
    dfs(x, y)
print(ans)

=======
Suggestion 6

def dfs(x,y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if not (x,y) in d:
        return
    if d[(x,y)]:
        return
    d[(x,y)] = True
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

n = int(input())
d = {}
for i in range(n):
    x,y = map(int,input().split())
    d[(x,y)] = False
ans = 0
for i in range(n):
    x,y = map(int,input().split())
    if d[(x,y)]:
        continue
    ans += 1
    dfs(x,y)
print(ans)

=======
Suggestion 7

def dfs(x,y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if (x,y) in black:
        black.remove((x,y))
        dfs(x-1,y-1)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x+1,y+1)

N = int(input())
black = set()
for _ in range(N):
    x,y = map(int,input().split())
    black.add((x,y))

ans = 0
while len(black) > 0:
    x,y = black.pop()
    dfs(x,y)
    ans += 1

print(ans)

=======
Suggestion 8

def dfs(x, y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if (x, y) in black:
        return
    black.add((x, y))
    dfs(x - 1, y - 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x + 1, y)
    dfs(x + 1, y + 1)


n = int(input())
black = set()
for _ in range(n):
    x, y = map(int, input().split())
    dfs(x, y)
print(len(black))

=======
Suggestion 9

def dfs(x,y):
    if x<0 or x>=2000 or y<0 or y>=2000:
        return
    if grid[x][y]==0:
        return
    grid[x][y]=0
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

N=int(input())
grid=[[0]*2000 for i in range(2000)]
for i in range(N):
    x,y=map(int,input().split())
    x+=1000
    y+=1000
    grid[x][y]=1

ans=0
for i in range(2000):
    for j in range(2000):
        if grid[i][j]==1:
            dfs(i,j)
            ans+=1
print(ans)

=======
Suggestion 10

def dfs(x,y):
    global visited, black
    visited[x][y] = True
    black.append((x,y))

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 2002 and 0 <= ny < 2002:
            if not visited[nx][ny] and grid[nx][ny] == '#':
                dfs(nx,ny)

N = int(input())
grid = [['.'] * 2002 for _ in range(2002)]
visited = [[False] * 2002 for _ in range(2002)]
dx = [-1,-1,0,0,1,1]
dy = [-1,0,-1,1,0,1]
black = []

for _ in range(N):
    x,y = map(int,input().split())
    x += 1001
    y += 1001
    grid[x][y] = '#'

ans = 0

for i in range(2002):
    for j in range(2002):
        if not visited[i][j] and grid[i][j] == '#':
            dfs(i,j)
            ans += 1

print(ans)
