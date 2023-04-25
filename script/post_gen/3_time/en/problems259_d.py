Synthesizing 10/10 solutions

=======
Suggestion 1

def dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

=======
Suggestion 2

def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x = []
    y = []
    r = []
    for i in range(N):
        x_i, y_i, r_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        r.append(r_i)
    if N == 1:
        if (s_x - x[0])**2 + (s_y - y[0])**2 < r[0]**2 and (t_x - x[0])**2 + (t_y - y[0])**2 < r[0]**2:
            print('Yes')
        else:
            print('No')
    else:
        if (s_x - x[0])**2 + (s_y - y[0])**2 < r[0]**2:
            for i in range(1, N):
                if (t_x - x[i])**2 + (t_y - y[i])**2 < r[i]**2:
                    print('Yes')
                    exit()
        elif (s_x - x[1])**2 + (s_y - y[1])**2 < r[1]**2:
            for i in range(1, N):
                if (t_x - x[i])**2 + (t_y - y[i])**2 < r[i]**2:
                    print('Yes')
                    exit()
        else:
            print('No')

=======
Suggestion 3

def get_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

=======
Suggestion 4

def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]
    circles.append([s_x, s_y, 0])
    circles.append([t_x, t_y, 0])
    N += 2
    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1, r1 = circles[i]
            x2, y2, r2 = circles[j]
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if d <= r1 + r2:
                graph[i][j] = 1
                graph[j][i] = 1
    seen = [False] * N
    def dfs(v):
        seen[v] = True
        for i in range(N):
            if graph[v][i] == 1 and seen[i] == False:
                dfs(i)
    dfs(N - 2)
    if seen[N - 1]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [tuple(map(int, input().split())) for _ in range(N)]

    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def in_circle(x, y, circle):
        return dist(x, y, circle[0], circle[1]) <= circle[2]

    def dfs(x, y, circles):
        if in_circle(x, y, circles[0]):
            return True
        if len(circles) == 1:
            return False
        return dfs(x, y, circles[1:]) or dfs(x, y, circles[1:])

    print('Yes' if dfs(s_x, s_y, circles) and dfs(t_x, t_y, circles) else 'No')

=======
Suggestion 6

def main():
    #input
    N = int(input())
    s_x,s_y,t_x,t_y = map(int,input().split())
    circles = []
    for i in range(N):
        x,y,r = map(int,input().split())
        circles.append([x,y,r])

    #solve
    def dist(x1,y1,x2,y2):
        return ((x1-x2)**2+(y1-y2)**2)**0.5
    def dist2(x1,y1,x2,y2):
        return (x1-x2)**2+(y1-y2)**2
    def is_in(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) < r**2
    def is_on(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) == r**2
    def is_cross(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) < r**2 and dist2(x1,y1,x2,y2) > 0
    def is_cross2(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) < r**2 and dist2(x1,y1,x2,y2) == 0
    def is_cross3(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) == r**2 and dist2(x1,y1,x2,y2) > 0
    def is_cross4(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) > r**2 and dist2(x1,y1,x2,y2) > 0

    def is_cross_circle(x1,y1,x2,y2,x3,y3,r):
        if is_in(x1,y1,x3,y3,r):
            return True
        elif is_in(x2,y2,x3,y3,r):
            return True
        elif is_on(x1,y1,x3,y3,r):
            return True
        elif is_on(x2,y2,x3,y3,r):
            return True
        elif is_cross(x1,y1,x2,y2,r):
            if is_cross4(x1,y1,x3,y3,r)

=======
Suggestion 7

def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]
    # print(circles)

    # 2点間の距離を求める
    def dist(x1, y1, x2, y2):
        return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    # 2点間の距離が円の半径より大きければOK
    for x, y, r in circles:
        if dist(s_x, s_y, x, y) <= r and dist(t_x, t_y, x, y) <= r:
            print("No")
            exit()

    print("Yes")

=======
Suggestion 8

def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    circles = [tuple(map(int, input().split())) for _ in range(N)]
    # print(N, s_x, s_y, t_x, t_y, circles)

    def dist2(x1, y1, x2, y2):
        return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)

    def in_circle(x, y, circle):
        x0, y0, r = circle
        return dist2(x, y, x0, y0) <= r * r

    def dfs(x, y, visited):
        if in_circle(x, y, circles[0]): return True
        if in_circle(x, y, circles[1]): return True
        if in_circle(x, y, circles[2]): return True
        if in_circle(x, y, circles[3]): return True
        visited.add((x, y))
        for cx, cy, cr in circles:
            dx = cx - x
            dy = cy - y
            if dx == 0 and dy == 0: continue
            if dx == 0:
                if dy > 0:
                    nx = x
                    ny = y + cr
                else:
                    nx = x
                    ny = y - cr
            elif dy == 0:
                if dx > 0:
                    nx = x + cr
                    ny = y
                else:
                    nx = x - cr
                    ny = y
            else:
                if dx > 0:
                    nx = x + cr
                else:
                    nx = x - cr
                if dy > 0:
                    ny = y + cr
                else:
                    ny = y - cr
            if (nx, ny) in visited: continue
            if dfs(nx, ny, visited): return True
        return False

    if dfs(s_x, s_y, set()):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 9

def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    xyr = [list(map(int, input().split())) for _ in range(N)]
    #print(xyr)

    def dist(x1, y1, x2, y2):
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

    def is_in_circle(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) <= xyr[2]

    def is_in_circle2(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) < xyr[2]

    def is_on_circle(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2]

    def is_on_circle2(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] - 10**(-6)

    def is_in_circle3(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) < xyr[2] - 10**(-6)

    def is_on_circle3(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] - 10**(-6)

    def is_on_circle4(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] + 10**(-6)

    def is_on_circle5(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] + 10**(-6)

    def is_on_circle6(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) == xyr[2] - 10**(-6)

    def is_in_circle4(x, y, xyr):
        return dist(x, y, xyr[0], xyr[1]) < xyr[2] + 10**(-6)

    def is_in_circle5

=======
Suggestion 10

def main():
    import sys
    from math import sqrt
    import numpy as np
    from scipy.sparse.csgraph import floyd_warshall
    from scipy.sparse import csr_matrix

    readline = sys.stdin.readline

    N = int(readline())
    sx, sy, tx, ty = map(int, readline().split())
    X = np.zeros((N, 2), dtype=np.int64)
    R = np.zeros(N, dtype=np.int64)
    for i in range(N):
        x, y, r = map(int, readline().split())
        X[i] = np.array([x, y])
        R[i] = r

    # 2点間の距離
    def dist(x1, y1, x2, y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)

    # 2点間の距離がr1+r2以下かどうか
    def is_ok(x1, y1, r1, x2, y2, r2):
        return dist(x1, y1, x2, y2) <= r1+r2

    # 2点間の距離がr1+r2以下なら1, そうでなければINF
    def weight(x1, y1, r1, x2, y2, r2):
        return 1 if is_ok(x1, y1, r1, x2, y2, r2) else float('inf')

    # 2点間の距離がr1+r2以下なら1, そうでなければ0
    def weight2(x1, y1, r1, x2, y2, r2):
        return 1 if is_ok(x1, y1, r1, x2, y2, r2) else 0

    # 隣接行列
    W = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        for j in range(N):
            W[i, j] = weight2(X[i, 0], X[i, 1], R[i], X[j, 0], X[j, 1], R[j])

    # 隣接行列から最
