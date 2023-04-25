Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    minx = X[0]
    miny = Y[0]
    maxx = X[N-1]
    maxy = Y[N-1]
    #print(minx, miny, maxx, maxy)
    #print(X, Y)
    #print(X[0], X[N-1], Y[0], Y[N-1])
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)
    #print(X[0]-1, X[N-1]+1, Y[0]-1, Y[N-1]+1)

    print(maxx-minx+1+maxy-miny+1-2)

=======
Suggestion 2

def main():
    n = int(input())
    black = set()
    for i in range(n):
        x, y = map(int, input().split())
        black.add((x, y))
    ans = 0
    while len(black) > 0:
        ans += 1
        x, y = black.pop()
        q = [(x, y)]
        while len(q) > 0:
            x, y = q.pop()
            if (x - 1, y - 1) in black:
                black.remove((x - 1, y - 1))
                q.append((x - 1, y - 1))
            if (x - 1, y) in black:
                black.remove((x - 1, y))
                q.append((x - 1, y))
            if (x, y - 1) in black:
                black.remove((x, y - 1))
                q.append((x, y - 1))
            if (x, y + 1) in black:
                black.remove((x, y + 1))
                q.append((x, y + 1))
            if (x + 1, y) in black:
                black.remove((x + 1, y))
                q.append((x + 1, y))
            if (x + 1, y + 1) in black:
                black.remove((x + 1, y + 1))
                q.append((x + 1, y + 1))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    x.sort()
    y.sort()
    #print(x)
    #print(y)
    if N % 2 == 0:
        min_x = (x[N//2-1] + x[N//2]) // 2
        max_x = min_x + 1
        min_y = (y[N//2-1] + y[N//2]) // 2
        max_y = min_y + 1
        #print(min_x, max_x, min_y, max_y)
        ans = (max_x - min_x + 1) * (max_y - min_y + 1)
    else:
        min_x = x[N//2]
        max_x = min_x
        min_y = y[N//2]
        max_y = min_y
        #print(min_x, max_x, min_y, max_y)
        ans = 1
    print(ans)

=======
Suggestion 4

def dfs(x,y):
    if (x,y) in visited:
        return
    visited.add((x,y))
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1)]:
        if (x+dx,y+dy) in black:
            dfs(x+dx,y+dy)

n = int(input())
black = set()
for _ in range(n):
    x,y = map(int,input().split())
    black.add((x,y))

visited = set()
ans = 0
for x,y in black:
    if (x,y) in visited:
        continue
    ans += 1
    dfs(x,y)
print(ans)

=======
Suggestion 5

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 6

def dfs(i,j):
    global visited
    visited[i][j] = True
    for k in range(6):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < 2001 and 0 <= nj < 2001 and visited[ni][nj] == False and grid[ni][nj] == '#':
            dfs(ni,nj)

N = int(input())
grid = [['.'] * 2001 for _ in range(2001)]
di = [-1,-1,0,0,1,1]
dj = [-1,0,-1,1,0,1]
for _ in range(N):
    X,Y = map(int,input().split())
    grid[X+1000][Y+1000] = '#'

visited = [[False] * 2001 for _ in range(2001)]
ans = 0
for i in range(2001):
    for j in range(2001):
        if visited[i][j] == False and grid[i][j] == '#':
            ans += 1
            dfs(i,j)
print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    black_cells = []
    for i in range(N):
        x,y = map(int,input().split())
        black_cells.append((x,y))
    black_cells.sort()
    black_cells = list(set(black_cells))
    print(black_cells)
    return

=======
Suggestion 8

def check_black_neighbours(x, y):
    if (x-1,y-1) in black_cells:
        return True
    if (x-1,y) in black_cells:
        return True
    if (x,y-1) in black_cells:
        return True
    if (x,y+1) in black_cells:
        return True
    if (x+1,y) in black_cells:
        return True
    if (x+1,y+1) in black_cells:
        return True
    return False

black_cells = []
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    black_cells.append((x,y))

=======
Suggestion 9

def main():
    N = int(input())
    black = [tuple(map(int, input().split())) for _ in range(N)]
    black = set(black)

    visited = set()
    def dfs(i, j):
        if (i, j) in visited:
            return
        visited.add((i, j))

        for di, dj in [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]:
            next_i = i + di
            next_j = j + dj
            if (next_i, next_j) in black:
                dfs(next_i, next_j)

    ans = 0
    for i, j in black:
        if (i, j) in visited:
            continue
        dfs(i, j)
        ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    cells = []
    for i in range(N):
        cells.append([int(x) for x in input().split(' ')])
    cells.sort()
    cells = [cells[0]] + [cells[i] for i in range(1, N) if cells[i] != cells[i-1]]
    print(len(cells))
