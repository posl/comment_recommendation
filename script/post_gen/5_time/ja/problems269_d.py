Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if abs(X[i]-X[j]) <= 1 and abs(Y[i]-Y[j]) <= 1:
                ans += 1
    print(ans)
main()

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
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

N = int(input())
grid = [[0] * 2000 for _ in range(2000)]
visited = [[False] * 2000 for _ in range(2000)]
for _ in range(N):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    grid[x][y] = 1
ans = 0
for x in range(2000):
    for y in range(2000):
        if grid[x][y] == 0 or visited[x][y]:
            continue
        ans += 1
        dfs(x, y)
print(ans)

=======
Suggestion 3

def dfs(x, y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000 or grid[x][y] == 0:
        return
    grid[x][y] = 0
    dfs(x-1, y-1)
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    dfs(x+1, y)
    dfs(x+1, y+1)

n = int(input())
grid = [[0]*2000 for _ in range(2000)]
for _ in range(n):
    x, y = map(int, input().split())
    grid[x+1000][y+1000] = 1

ans = 0
for i in range(2000):
    for j in range(2000):
        if grid[i][j] == 1:
            dfs(i, j)
            ans += 1
print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    d = {}
    for i in range(n):
        x, y = map(int, input().split())
        d[(x, y)] = True
    ans = 0
    for k in d:
        x, y = k
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j:
                    continue
                if d.get((x + i, y + j)):
                    ans += 1
                    break
    print(ans // 2)

=======
Suggestion 5

def dfs(i, j, visited):
    if visited[i][j] == True:
        return
    visited[i][j] = True
    for k in range(6):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 2001 and 0 <= nj < 2001:
            dfs(ni, nj, visited)

N = int(input())
di = [-1, -1, 0, 0, 1, 1]
dj = [-1, 0, -1, 1, 0, 1]
visited = [[False] * 2001 for _ in range(2001)]
for _ in range(N):
    x, y = map(int, input().split())
    visited[x + 1000][y + 1000] = True
ans = 0
for i in range(2001):
    for j in range(2001):
        if visited[i][j] == True:
            dfs(i, j, visited)
            ans += 1
print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    xy.sort()
    #print(xy)
    ans = 1
    for i in range(n-1):
        if xy[i][0] == xy[i+1][0]:
            if xy[i][1] != xy[i+1][1]:
                ans += 1
        elif xy[i][1] == xy[i+1][1]:
            if xy[i][0] != xy[i+1][0]:
                ans += 1
        else:
            ans += 1
    print(ans)

=======
Suggestion 7

def solve():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    x.sort()
    y.sort()
    x_min = x[0]
    x_max = x[n-1]
    y_min = y[0]
    y_max = y[n-1]
    x_min -= 1
    x_max += 1
    y_min -= 1
    y_max += 1
    x.append(x_min)
    x.append(x_max)
    y.append(y_min)
    y.append(y_max)
    x.sort()
    y.sort()
    n += 2
    x_min_idx = x.index(x_min)
    x_max_idx = x.index(x_max)
    y_min_idx = y.index(y_min)
    y_max_idx = y.index(y_max)
    #print(x)
    #print(y)
    #print(x_min_idx)
    #print(x_max_idx)
    #print(y_min_idx)
    #print(y_max_idx)
    #print(n)
    grid = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        grid[i][i] = 1
    for i in range(n-1):
        grid[i][i+1] = 1
        grid[i+1][i] = 1
    for i in range(n-2):
        grid[i][i+2] = 1
        grid[i+2][i] = 1
    for i in range(n-3):
        grid[i][i+3] = 1
        grid[i+3][i] = 1
    for i in range(n-4):
        grid[i][i+4] = 1
        grid[i+4][i] = 1
    for i in range(n-5):
        grid[i][i+5] = 1
        grid[i+5][i] = 1
    #print(grid)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                if (x_min_idx <= i and i <= x_max_idx) and (y_min_idx <= j and j <= y_max_idx

=======
Suggestion 8

def dfs(x, y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000:
        return
    if c[y][x] == 0:
        return
    if visited[y][x]:
        return
    visited[y][x] = True
    dfs(x - 1, y - 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x + 1, y)
    dfs(x + 1, y + 1)

n = int(input())
c = [[0 for _ in range(2000)] for _ in range(2000)]
visited = [[False for _ in range(2000)] for _ in range(2000)]
for _ in range(n):
    x, y = map(int, input().split())
    c[y + 1000][x + 1000] = 1

ans = 0
for i in range(2000):
    for j in range(2000):
        if c[i][j] == 1 and visited[i][j] == False:
            ans += 1
            dfs(j, i)
print(ans)

=======
Suggestion 9

def dfs(x,y):
    if x<0 or x>=1000 or y<0 or y>=1000:
        return
    if field[x][y] == 0:
        return
    field[x][y] = 0
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)

n = int(input())
field = [[0]*1000 for _ in range(1000)]
for _ in range(n):
    x,y = map(int,input().split())
    field[x][y] = 1

ans = 0
for i in range(1000):
    for j in range(1000):
        if field[i][j] == 1:
            dfs(i,j)
            ans += 1
print(ans)

=======
Suggestion 10

def dfs(x, y):
    if x < 0 or x >= 2001 or y < 0 or y >= 2001:
        return
    if c[y][x]:
        return
    c[y][x] = True
    dfs(x - 1, y - 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x + 1, y)
    dfs(x + 1, y + 1)

n = int(input())
c = [[False] * 2001 for _ in range(2001)]
for _ in range(n):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    c[y][x] = True
ans = 0
for y in range(2001):
    for x in range(2001):
        if not c[y][x]:
            continue
        if c[y - 1][x - 1] or c[y - 1][x] or c[y][x - 1] or c[y][x + 1] or c[y + 1][x] or c[y + 1][x + 1]:
            continue
        ans += 1
        dfs(x, y)
print(ans)
