Synthesizing 10/10 solutions

=======
Suggestion 1

def search(a, b):
    if (a, b) in black:
        black.remove((a, b))
        search(a-1, b-1)
        search(a-1, b)
        search(a, b-1)
        search(a, b+1)
        search(a+1, b)
        search(a+1, b+1)

N = int(input())
black = set()
for i in range(N):
    a, b = map(int, input().split())
    black.add((a, b))

ans = 0
while len(black) > 0:
    a, b = black.pop()
    search(a, b)
    ans += 1

print(ans)

=======
Suggestion 2

def main():
    print("")

=======
Suggestion 3

def dfs(x,y):
    #print(x,y)
    if x < 0 or x >= 1000 or y < 0 or y >= 1000:
        return
    if grid[x][y] == 0:
        return
    if visited[x][y] == 1:
        return
    visited[x][y] = 1
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

N = int(input())
grid = [[0 for _ in range(1000)] for _ in range(1000)]
visited = [[0 for _ in range(1000)] for _ in range(1000)]
for i in range(N):
    x,y = map(int,input().split())
    grid[x][y] = 1
ans = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
            ans += 1
print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    #print(n)
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    #print(x)
    #print(y)
    #print(x[0])
    #print(y[0])
    #print(x[1])
    #print(y[1])
    #print(x[2])
    #print(y[2])
    #print(x[3])
    #print(y[3])
    #print(x[4])
    #print(y[4])
    #print(x[5])
    #print(y[5])
    #print(x[6])
    #print(y[6])
    #print(x[7])
    #print(y[7])
    #print(x[8])
    #print(y[8])
    #print(x[9])
    #print(y[9])
    #print(x[10])
    #print(y[10])
    #print(x[11])
    #print(y[11])
    #print(x[12])
    #print(y[12])
    #print(x[13])
    #print(y[13])
    #print(x[14])
    #print(y[14])
    #print(x[15])
    #print(y[15])
    #print(x[16])
    #print(y[16])
    #print(x[17])
    #print(y[17])
    #print(x[18])
    #print(y[18])
    #print(x[19])
    #print(y[19])
    #print(x[20])
    #print(y[20])
    #print(x[21])
    #print(y[21])
    #print(x[22])
    #print(y[22])
    #print(x[23])
    #print(y[23])
    #print(x[24])
    #print(y[24])
    #print(x[25])
    #print(y[25])
    #print(x[26])
    #print(y[26])
    #print(x[27])
    #print(y[27])
    #print(x[28])
    #print(y[28])
    #print(x[29])
    #print(y[29])
    #print(x[30])
    #print(y[30])
    #print(x[31])

=======
Suggestion 5

def find(x, y):
    if (x, y) in black:
        black.remove((x, y))
        find(x - 1, y - 1)
        find(x - 1, y)
        find(x, y - 1)
        find(x, y + 1)
        find(x + 1, y)
        find(x + 1, y + 1)
        return True
    return False

n = int(input())
black = set()
for _ in range(n):
    x, y = map(int, input().split())
    black.add((x, y))

ans = 0
while black:
    x, y = black.pop()
    if find(x, y):
        ans += 1
print(ans)

=======
Suggestion 6

def dfs(i, j):
    global visited, black
    visited[i][j] = True
    for k in range(6):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 2001 and 0 <= nj < 2001:
            if black[ni][nj] == 1 and not visited[ni][nj]:
                dfs(ni, nj)

n = int(input())
di = [-1, -1, 0, 0, 1, 1]
dj = [-1, 0, -1, 1, 0, 1]
black = [[0] * 2001 for _ in range(2001)]
visited = [[False] * 2001 for _ in range(2001)]
for _ in range(n):
    x, y = map(int, input().split())
    black[x + 1000][y + 1000] = 1

ans = 0
for i in range(2001):
    for j in range(2001):
        if black[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            ans += 1
print(ans)

=======
Suggestion 7

def dfs(x,y):
    if (x,y) in visited:
        return
    visited.add((x,y))
    for dx,dy in d:
        dfs(x+dx,y+dy)

n = int(input())
d = [(0,-1),(-1,0),(-1,-1),(0,1),(1,0),(1,1)]
visited = set()
for i in range(n):
    x,y = map(int,input().split())
    dfs(x,y)
print(len(visited))

=======
Suggestion 8

def dfs(i, j, n):
    if i < 0 or i >= n or j < 0 or j >= n:
        return
    if grid[i][j] == 0:
        return
    grid[i][j] = 0
    dfs(i-1, j-1, n)
    dfs(i-1, j, n)
    dfs(i, j-1, n)
    dfs(i, j+1, n)
    dfs(i+1, j, n)
    dfs(i+1, j+1, n)

=======
Suggestion 9

def dfs(x, y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000:
        return
    if c[x][y] == 0:
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
c = [[0] * 2000 for _ in range(2000)]
visited = [[False] * 2000 for _ in range(2000)]
for i in range(n):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    c[x][y] = 1

ans = 0
for i in range(2000):
    for j in range(2000):
        if c[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            ans += 1

print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    print(n)
