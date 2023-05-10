Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    cx = []
    cy = []
    cr = []
    for _ in range(N):
        x, y, r = map(int, input().split())
        cx.append(x)
        cy.append(y)
        cr.append(r)
    #print(N, sx, sy, tx, ty)
    #print(cx, cy, cr)
    #print('------------------')
    #print('------------------')

=======
Suggestion 2

def solve():
    return

=======
Suggestion 3

def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(N)]
    xyr = [[x, y, r] for x, y, r in xyr]
    #print(xyr)

    def is_reachable(xyr):
        def is_in_circle(x, y, r):
            #print(x, y, r)
            return (x - s_x) ** 2 + (y - s_y) ** 2 <= r ** 2 and (x - t_x) ** 2 + (y - t_y) ** 2 <= r ** 2

        for x, y, r in xyr:
            if is_in_circle(x, y, r):
                return True

        return False

    print("Yes" if is_reachable(xyr) else "No")

main()

=======
Suggestion 4

def main():
    # N = int(input())
    # sx, sy, tx, ty = map(int, input().split())
    # circles = [list(map(int, input().split())) for _ in range(N)]
    N = 4
    sx, sy, tx, ty = 0, -2, 3, 3
    circles = [[0, 0, 2], [2, 0, 2], [2, 3, 1], [-3, 3, 3]]

    # N = 3
    # sx, sy, tx, ty = 0, 1, 0, 3
    # circles = [[0, 0, 1], [0, 0, 2], [0, 0, 3]]

    # N = 3
    # sx, sy, tx, ty = 0, 1, 0, 3
    # circles = [[0, 0, 1], [0, 0, 2], [0, 0, 3]]

    # N = 3
    # sx, sy, tx, ty = 0, 1, 0, 3
    # circles = [[0, 0, 1], [0, 0, 2], [0, 0, 3]]

    # N = 3
    # sx, sy, tx, ty = 0, 1, 0, 3
    # circles = [[0, 0, 1], [0, 0, 2], [0, 0, 3]]

    # N = 3
    # sx, sy, tx, ty = 0, 1, 0, 3
    # circles = [[0, 0, 1], [0, 0, 2], [0, 0, 3]]

    # N = 3
    # sx, sy, tx, ty = 0, 1, 0, 3
    # circles = [[0, 0, 1], [0, 0, 2], [0, 0, 3]]

    # N = 3
    # sx, sy, tx, ty = 0, 1, 0, 3

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]

    def check(x, y):
        for circle in circles:
            if (x - circle[0])**2 + (y - circle[1])**2 >= circle[2]**2:
                return False
        return True

    def bfs():
        from collections import deque
        q = deque()
        q.append((s_x, s_y))
        visited = set()
        while q:
            x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if check(nx, ny) and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))
        return (t_x, t_y) in visited

    print("Yes" if bfs() else "No")

=======
Suggestion 7

def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    if ((sx, sy), (tx, ty)) in [(c1, c2) for c1 in circles for c2 in circles]:
        print('Yes')
        return

    def is_connected((x1, y1), (x2, y2), r):
        d = ((x1-x2)**2+(y1-y2)**2)**0.5
        if d <= r:
            return True
        return False

    def dfs(i, visited):
        if i == tx and j == ty:
            return True
        for j in range(n):
            if j in visited:
                continue
            if is_connected((i, j), (tx, ty), circles[j][2]):
                return dfs(j, visited + [j])
        return False

    for i in range(n):
        if is_connected((sx, sy), (circles[i][0], circles[i][1]), circles[i][2]):
            if dfs(i, [i]):
                print('Yes')
                return
    print('No')

=======
Suggestion 8

def solve():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(N)]
    xyr.append([s_x, s_y, 0])
    xyr.append([t_x, t_y, 0])
    N += 2

    def check(i, j):
        xi, yi, ri = xyr[i]
        xj, yj, rj = xyr[j]
        d = ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5
        return d <= ri + rj

    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if check(i, j):
                graph[i][j] = 1
                graph[j][i] = 1

    from collections import deque
    def bfs(s):
        INF = 10 ** 18
        dist = [INF] * N
        dist[s] = 0
        que = deque([s])
        while que:
            v = que.popleft()
            for nv in range(N):
                if graph[v][nv] and dist[nv] == INF:
                    dist[nv] = dist[v] + 1
                    que.append(nv)
        return dist

    dist = bfs(N - 2)
    if dist[N - 1] == INF:
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def f():
    import sys
    import math
    input = sys.stdin.readline
    def is_cross(x1, y1, r1, x2, y2, r2):
        d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if d < r1+r2 and d > abs(r1-r2):
            return True
        else:
            return False

    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    if sx == tx and sy == ty:
        print("Yes")
        exit()
    xl = []
    yl = []
    rl = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        xl.append(x)
        yl.append(y)
        rl.append(r)
    for i in range(n):
        if is_cross(sx, sy, rl[i], tx, ty, 0):
            print("Yes")
            exit()
    for i in range(n):
        for j in range(i+1, n):
            if is_cross(xl[i], yl[i], rl[i], xl[j], yl[j], rl[j]):
                print("Yes")
                exit()
    print("No")
f()

=======
Suggestion 10

def check(x,y):
    if x**2+y**2 <= 1:
        return True
    else:
        return False
