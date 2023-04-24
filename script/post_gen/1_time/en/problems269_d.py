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
    print(N)

=======
Suggestion 2

def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    # 1. (x, y) -> (x, y + x) -> (x - y, 2x + y)
    X2 = [0] * N
    Y2 = [0] * N
    for i in range(N):
        X2[i] = X[i] - Y[i]
        Y2[i] = 2 * X[i] + Y[i]

    # 2. (x, y) -> (x + y, y) -> (2x + y, x - y)
    X3 = [0] * N
    Y3 = [0] * N
    for i in range(N):
        X3[i] = 2 * X[i] + Y[i]
        Y3[i] = X[i] - Y[i]

    # 3. (x, y) -> (x, y - x) -> (x + y, -2x + y)
    X4 = [0] * N
    Y4 = [0] * N
    for i in range(N):
        X4[i] = X[i] + Y[i]
        Y4[i] = -2 * X[i] + Y[i]

    # 4. (x, y) -> (x - y, y) -> (-2x + y, x + y)
    X5 = [0] * N
    Y5 = [0] * N
    for i in range(N):
        X5[i] = -2 * X[i] + Y[i]
        Y5[i] = X[i] + Y[i]

    # 5. (x, y) -> (x, -y) -> (-x, -y)
    X6 = [0] * N
    Y6 = [0] * N
    for i in range(N):
        X6[i] = -X[i]
        Y6[i] = -Y[i]

    # 6. (x, y) -> (-x, y) -> (-x, -y)
    X7 = [0] * N
    Y7 = [0

=======
Suggestion 3

def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i],Y[i] = map(int,input().split())
    print(N)

=======
Suggestion 4

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #print(X)
    #print(Y)
    #print(N)
    #print(X)
    #print(Y)
    #print("N =", N)
    #print("X =", X)
    #print("Y =", Y)
    #print("X =", X)
    #print("Y =", Y)
    #print("N =", N)
    #print("X =", X)
    #print("Y =", Y)
    #print("X =", X)
    #print("Y =", Y)
    #pri

=======
Suggestion 5

def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            x = X[i] - X[j]
            y = Y[i] - Y[j]
            for k in range(N):
                if k == i or k == j:
                    continue
                if x + X[k] == X[j] and y + Y[k] == Y[j]:
                    break
            else:
                ans += 1
    print(ans//3)

=======
Suggestion 6

def main():
    # Read input
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    # Get the set of all possible moves
    moves = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            moves.add((i, j))

    # Get the set of all possible moves
    moves = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            moves.add((i, j))

    # Get the set of all possible moves
    moves = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            moves.add((i, j))

    # Get the set of all possible moves
    moves = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            moves.add((i, j))

    # Get the set of all possible moves
    moves = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            moves.add((i, j))

    # Get the set of all possible moves
    moves = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            moves.add((i, j))

    # Get the set of all possible moves
    moves = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            moves.add((i, j))

    # Get the set of all possible moves
    moves = set()
    for i in range(-1, 2):
        for j in

=======
Suggestion 7

def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    n = int(input())
    xd = [0, 0, 1, 1, -1, -1]
    yd = [-1, 1, -1, 0, 0, 1]
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    xy = set(xy)
    visited = set()
    ans = 0
    for x, y in xy:
        if (x, y) in visited:
            continue
        ans += 1
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            visited.add((x, y))
            for dx, dy in zip(xd, yd):
                nx, ny = x + dx, y + dy
                if (nx, ny) in xy and (nx, ny) not in visited:
                    q.append((nx, ny))
    print(ans)

=======
Suggestion 8

def main():
    from collections import defaultdict
    from collections import deque
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    N = int(input())
    x = [0]*N
    y = [0]*N
    for i in range(N):
        x[i], y[i] = map(int, input().split())
    #print(x)
    #print(y)
    #print("N = ", N)
    #print("x = ", x)
    #print("y = ", y)
    #print("x[0] = ", x[0])
    #print("y[0] = ", y[0])
    #print("x[1] = ", x[1])
    #print("y[1] = ", y[1])
    #print("x[2] = ", x[2])
    #print("y[2] = ", y[2])
    #print("x[3] = ", x[3])
    #print("y[3] = ", y[3])
    #print("x[4] = ", x[4])
    #print("y[4] = ", y[4])
    #print("x[5] = ", x[5])
    #print("y[5] = ", y[5])
    #print("x[6] = ", x[6])
    #print("y[6] = ", y[6])
    #print("x[7] = ", x[7])
    #print("y[7] = ", y[7])
    #print("x[8] = ", x[8])
    #print("y[8] = ", y[8])
    #print("x[9] = ", x[9])
    #print("y[9] = ", y[9])
    #print("x[10] = ", x[10])
    #print("y[10] = ", y[10])
    #print("x[11] = ", x[11])
    #print("y[11] = ", y[11])
    #print("x[12] = ", x[12])
    #print("y[12] = ", y[12])
    #print("x[13] = ", x[13])
    #print("y

=======
Suggestion 9

def add(a,b):
  return (a[0]+b[0],a[1]+b[1])

=======
Suggestion 10

def main():
    # Get input
    n = int(input())
    coords = []
    for i in range(n):
        x, y = map(int, input().split())
        coords.append((x, y))
    # Get all the hexagons
    hexagons = set()
    for x, y in coords:
        hexagons.add((x, y))
        hexagons.add((x + 1, y))
        hexagons.add((x - 1, y))
        hexagons.add((x, y + 1))
        hexagons.add((x, y - 1))
        hexagons.add((x + 1, y - 1))
        hexagons.add((x - 1, y + 1))
    # Get all the connected components
    components = []
    while hexagons:
        component = set()
        # Get the first hexagon
        hexagon = hexagons.pop()
        component.add(hexagon)
        # Get all the connected hexagons
        while component:
            new_hexagon = component.pop()
            for x, y in [(new_hexagon[0] + 1, new_hexagon[1]),
                         (new_hexagon[0] - 1, new_hexagon[1]),
                         (new_hexagon[0], new_hexagon[1] + 1),
                         (new_hexagon[0], new_hexagon[1] - 1),
                         (new_hexagon[0] + 1, new_hexagon[1] - 1),
                         (new_hexagon[0] - 1, new_hexagon[1] + 1)]:
                if x in range(-1001, 1002) and y in range(-1001, 1002):
                    if x % 2 == 0 and y % 2 == 0:
                        if (x, y) in hexagons:
                            component.add((x, y))
                            hexagons.remove((x, y))
        components.append(component)
    # Print the answer
    print(len(components))
