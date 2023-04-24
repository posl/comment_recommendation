Synthesizing 10/10 solutions

=======
Suggestion 1

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

=======
Suggestion 2

def bfs(sx, sy):
    dist = [[-1] * N for _ in range(N)]
    dist[sx][sy] = 0
    que = deque([(sx, sy)])
    while que:
        x, y = que.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))
    return dist

N, M = map(int, input().split())
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dist = bfs(0, 0)
for i in range(N):
    for j in range(N):
        if dist[i][j] == -1:
            print(-1, end=" ")
        else:
            print(dist[i][j] // 2 + 1, end=" ")
    print()

=======
Suggestion 3

def main():
    n, m = map(int, raw_input().split())
    dist = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = (i - 0) ** 2 + (j - 0) ** 2
    for i in range(n):
        for j in range(n):
            if dist[i][j] == m:
                print 1
            elif dist[i][j] < m:
                print 2
            else:
                print -1

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    if m == 1:
        for i in range(n):
            for j in range(n):
                print(0 if i == j else 1)
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    print(0)
                elif j == 0:
                    print(i+1)
                elif i == 0:
                    print(j+1)
                else:
                    print(min(i+1,j+1))

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = list(map(int,input().split()))
    d = list(map(int,input().split()))
    e = list(map(int,input().split()))
    f = list(map(int,input().split()))
    g = list(map(int,input().split()))
    h = list(map(int,input().split()))
    i = list(map(int,input().split()))
    j = list(map(int,input().split()))
    k = list(map(int,input().split()))
    l = list(map(int,input().split()))
    m = list(map(int,input().split()))
    n = list(map(int,input().split()))
    o = list(map(int,input().split()))
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))
    r = list(map(int,input().split()))
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    u = list(map(int,input().split()))
    v = list(map(int,input().split()))
    w = list(map(int,input().split()))
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    z = list(map(int,input().split()))
    aa = list(map(int,input().split()))
    ab = list(map(int,input().split()))
    ac = list(map(int,input().split()))
    ad = list(map(int,input().split()))
    ae = list(map(int,input().split()))
    af = list(map(int,input().split()))
    ag = list(map(int,input().split()))
    ah = list(map(int,input().split()))
    ai = list(map(int,input().split()))
    aj = list(map(int,input().split()))
    ak = list(map(int,input().split()))
    al = list(map(int,input().split()))
    am = list(map(int,input().split()))
    an = list(map(int,input().split()))
    ao = list(map(int,input().split()))
    ap = list(map(int,input().split()))
    aq = list(map(int,input().split()))
    ar = list(map(int,input().split()))
    as_ = list(map(int,input().split()))
    at = list(map(int,input().split()))
    au = list(map(int,input().split()))
    av = list(map(int,input().split()))
    aw = list(map(int

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    if n == 1:
        print(0)
        return
    elif m == 1:
        for i in range(n):
            print(i)
        return
    else:
        for i in range(n):
            for j in range(n):
                if i == j:
                    print(0,end="")
                elif i == 0:
                    print(j,end="")
                elif j == 0:
                    print(i,end="")
                else:
                    print(i+j,end="")
            print()

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    if n < 2 or n > 400 or m < 1 or m > 10**6:
        print("Wrong Input")
        return
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                print(0,end=' ')
            else:
                print(1,end=' ')
        print()

=======
Suggestion 8

def bfs(graph, start, end, nodes):
    queue = []
    queue.append(start)
    distance = {}
    distance[start] = 0
    while len(queue) > 0:
        current = queue.pop(0)
        for neighbor in graph[current]:
            if neighbor not in distance:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    if end in distance:
        return distance[end]
    else:
        return -1

=======
Suggestion 9

def find_min_dist(x,y,grid):
    if grid[x][y] != -1:
        return grid[x][y]
    else:
        min_dist = 1000000
        for i in range(N):
            for j in range(N):
                if grid[i][j] != -1:
                    dist = ((x-i)**2 + (y-j)**2)**0.5
                    if dist.is_integer():
                        min_dist = min(min_dist, grid[i][j] + dist)
        grid[x][y] = min_dist
        return min_dist

N,M = map(int, input().split())
grid = [[-1 for _ in range(N)] for _ in range(N)]
grid[0][0] = 0
for i in range(N):
    for j in range(N):
        find_min_dist(i,j,grid)
for row in grid:
    print(" ".join(map(str,row)))

=======
Suggestion 10

def get_input():
    return map(int, input().strip().split(' '))
