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
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = X[i], Y[i]
                x2, y2 = X[j], Y[j]
                x3, y3 = X[k], Y[k]
                if x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2) == 0:
                    ans += 1
    print(ans)

main()

=======
Suggestion 2

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    print(N)

=======
Suggestion 3

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())

    # (x, y) -> (x + y, x - y)
    # (x, y) -> (x + y, x - y + 2 * y)
    # (x, y) -> (x + y, x - y + 4 * y)
    # (x, y) -> (x + y, x - y + 6 * y)
    # (x, y) -> (x + y, x - y + 8 * y)
    # (x, y) -> (x + y, x - y + 10 * y)
    # ...
    # (x, y) -> (x + y, x - y + 2 * n * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 2) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 3) * y)
    # ...
    # (x, y) -> (x + y, x - y + 2 * (n + 1000) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1001) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1002) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1003) * y)
    # ...
    # (x, y) -> (x + y, x - y + 2 * (n + 1000) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1001) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 100

=======
Suggestion 4

def main():
    n = int(input())
    black = set()
    for i in range(n):
        x, y = map(int, input().split())
        black.add((x, y))
    ans = 0
    while black:
        ans += 1
        q = [black.pop()]
        while q:
            x, y = q.pop()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (1, -1), (-1, 0), (-1, 1)):
                if (x + dx, y + dy) in black:
                    q.append((x + dx, y + dy))
                    black.remove((x + dx, y + dy))
    print(ans)

=======
Suggestion 5

def main():
    #input
    N = int(input())
    Xs = [0]*N
    Ys = [0]*N
    for i in range(N):
        Xs[i], Ys[i] = map(int, input().split())
    
    #compute
    #白

=======
Suggestion 6

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 7

def main():
    import sys
    import collections
    N = int(sys.stdin.readline())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int, sys.stdin.readline().split())
        X.append(x)
        Y.append(y)

    #print(N)
    #print(X)
    #print(Y)
    #print(X[0])
    #print(Y[0])
    #print(X[1])
    #print(Y[1])

    #print("X[0]=",X[0])
    #print("Y[0]=",Y[0])
    #print("X[1]=",X[1])
    #print("Y[1]=",Y[1])

    #print("X[2]=",X[2])
    #print("Y[2]=",Y[2])
    #print("X[3]=",X[3])
    #print("Y[3]=",Y[3])

    #print("X[4]=",X[4])
    #print("Y[4]=",Y[4])
    #print("X[5]=",X[5])
    #print("Y[5]=",Y[5])

    #print("X[6]=",X[6])
    #print("Y[6]=",Y[6])
    #print("X[7]=",X[7])
    #print("Y[7]=",Y[7])

    #print("X[8]=",X[8])
    #print("Y[8]=",Y[8])
    #print("X[9]=",X[9])
    #print("Y[9]=",Y[9])

    #print("X[10]=",X[10])
    #print("Y[10]=",Y[10])
    #print("X[11]=",X[11])
    #print("Y[11]=",Y[11])

    #print("X[12]=",X[12])
    #print("Y[12]=",Y[12])
    #print("X[13]=",X[13])
    #print("Y[13]=",Y[13])

    #print("X[14]=",X[14])
    #print("Y[14]=",Y[14])
    #print("X[15]=",X[

=======
Suggestion 8

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    d = defaultdict(int)
    for x, y in XY:
        d[(x, y)] = 1
    ans = 0
    for x, y in XY:
        if d[(x, y)] == 1:
            ans += 1
            d[(x, y)] = 0
            stack = [(x, y)]
            while stack:
                x, y = stack.pop()
                for dx, dy in [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]:
                    if d[(x + dx, y + dy)] == 1:
                        d[(x + dx, y + dy)] = 0
                        stack.append((x + dx, y + dy))
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    # 2D array
    grid = [[0 for x in range(2001)] for y in range(2001)]
    for i in range(N):
        X, Y = map(int, input().split())
        X += 1000
        Y += 1000
        grid[X][Y] = 1

    def dfs(x, y):
        if x < 0 or 2000 < x or y < 0 or 2000 < y or grid[x][y] == 0:
            return
        grid[x][y] = 0
        dfs(x - 1, y - 1)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)

    ans = 0
    for i in range(2001):
        for j in range(2001):
            if grid[i][j] == 1:
                dfs(i, j)
                ans += 1
    print(ans)

=======
Suggestion 10

def read_ints():
    return list(map(int, input().split()))
