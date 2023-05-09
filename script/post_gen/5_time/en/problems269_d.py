Synthesizing 10/10 solutions

=======
Suggestion 1

def get_neighbours(i,j):
    neighbours = []
    neighbours.append((i-1,j-1))
    neighbours.append((i-1,j))
    neighbours.append((i,j-1))
    neighbours.append((i,j+1))
    neighbours.append((i+1,j))
    neighbours.append((i+1,j+1))
    return neighbours

=======
Suggestion 2

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    print(n)

=======
Suggestion 3

def get_adjacent_cells(i,j):
    return [(i-1,j-1),(i-1,j),(i,j-1),(i,j+1),(i+1,j),(i+1,j+1)]

=======
Suggestion 4

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    x_min = x[0]
    y_min = y[0]
    x_max = x[-1]
    y_max = y[-1]
    x_min -= 1
    y_min -= 1
    x_max += 1
    y_max += 1
    x = [x_min] + x + [x_max]
    y = [y_min] + y + [y_max]
    #print(x)
    #print(y)
    ans = 0
    for i in range(n+1):
        for j in range(n+1):
            if i == j == 0:
                continue
            if x[i] == x[i-1] or y[j] == y[j-1]:
                continue
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    x_min = x[0]
    x_max = x[-1]
    y_min = y[0]
    y_max = y[-1]
    ans = 0
    for i in range(x_min, x_max+1):
        for j in range(y_min, y_max+1):
            if (i+j)%2 == 0:
                continue
            else:
                if i in x and j in y:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        tmp_x, tmp_y = map(int, input().split())
        x.append(tmp_x)
        y.append(tmp_y)
    x_min = min(x)
    x_max = max(x)
    y_min = min(y)
    y_max = max(y)
    #print(x_min, x_max, y_min, y_max)
    cnt = 0
    for i in range(n):
        if x_min <= x[i] <= x_max and y_min <= y[i] <= y_max:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    x_min = min(X)
    x_max = max(X)
    y_min = min(Y)
    y_max = max(Y)
    x_range = x_max - x_min
    y_range = y_max - y_min
    x_range += 1
    y_range += 1
    if x_range > y_range:
        x_range, y_range = y_range, x_range
    if x_range == 1:
        print(1)
        exit()
    elif x_range == 2:
        print(2)
        exit()
    elif x_range == 3:
        if y_range == 3:
            print(2)
            exit()
        else:
            print(3)
            exit()
    elif x_range == 4:
        if y_range == 4:
            print(3)
            exit()
        else:
            print(4)
            exit()
    else:
        print(4)
        exit()

=======
Suggestion 8

def main():
    N = int(input())
    black = set()
    for _ in range(N):
        x, y = map(int, input().split())
        black.add((x, y))
    ans = 0
    while black:
        ans += 1
        q = [black.pop()]
        while q:
            x, y = q.pop()
            for dx, dy in [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]:
                if (x+dx, y+dy) in black:
                    q.append((x+dx, y+dy))
                    black.remove((x+dx, y+dy))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    a = [[0 for i in range(2001)] for j in range(2001)]
    for i in range(n):
        x, y = map(int, input().split())
        a[x+1000][y+1000] = 1
    dx = [1, 1, 0, -1, -1, 0]
    dy = [-1, 0, 1, 1, 0, -1]
    ans = 0
    for i in range(2001):
        for j in range(2001):
            if a[i][j] == 1:
                ans += 1
                q = []
                q.append([i, j])
                a[i][j] = 0
                while len(q) > 0:
                    x, y = q.pop()
                    for k in range(6):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < 2001 and 0 <= ny < 2001 and a[nx][ny] == 1:
                            q.append([nx, ny])
                            a[nx][ny] = 0
    print(ans)

=======
Suggestion 10

def dfs(i,j):
    global grid
    stack = [(i,j)]
    while stack:
        i,j = stack.pop()
        if grid[i][j] == 0:
            grid[i][j] = 1
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < 2002 and 0 <= nj < 2002:
                    if grid[ni][nj] == 0:
                        stack.append((ni,nj))
    return 1

N = int(input())
grid = [[0 for j in range(2002)] for i in range(2002)]
for _ in range(N):
    X,Y = map(int,input().split())
    grid[X+1000][Y+1000] = 2
ans = 0
for i in range(2002):
    for j in range(2002):
        if grid[i][j] == 2:
            ans += dfs(i,j)
print(ans)
