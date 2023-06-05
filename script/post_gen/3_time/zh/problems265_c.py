Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    h,w = map(int,input().split())
    g = [list(input()) for _ in range(h)]
    i,j = 0,0
    while g[i][j] != '.':
        if g[i][j] == 'U':
            if i == 0:
                print(-1)
                return
            i -= 1
        elif g[i][j] == 'D':
            if i == h - 1:
                print(-1)
                return
            i += 1
        elif g[i][j] == 'L':
            if j == 0:
                print(-1)
                return
            j -= 1
        elif g[i][j] == 'R':
            if j == w - 1:
                print(-1)
                return
            j += 1
    print(i+1,j+1)

=======
Suggestion 2

def main():
    H,W = map(int,input().split())
    G = []
    for i in range(H):
        G.append(input())
    i,j = 0,0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                print(i+1,j+1)
                break
            else:
                i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                print(i+1,j+1)
                break
            else:
                i += 1
        elif G[i][j] == 'L':
            if j == 0:
                print(i+1,j+1)
                break
            else:
                j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                print(i+1,j+1)
                break
            else:
                j += 1

=======
Suggestion 3

def path(H,W,G):
    i,j = 1,1
    while True:
        if G[i-1][j-1] == "U":
            if i == 1:
                return [i,j]
            else:
                i -= 1
        elif G[i-1][j-1] == "D":
            if i == H:
                return [i,j]
            else:
                i += 1
        elif G[i-1][j-1] == "L":
            if j == 1:
                return [i,j]
            else:
                j -= 1
        elif G[i-1][j-1] == "R":
            if j == W:
                return [i,j]
            else:
                j += 1
        else:
            return [-1,-1]

=======
Suggestion 4

def main():
    H,W = map(int,input().split())
    G = [input() for _ in range(H)]
    i = j = 0
    visited = [[0]*W for _ in range(H)]
    while True:
        if G[i][j] == 'U' and i != 0:
            i -= 1
        elif G[i][j] == 'D' and i != H-1:
            i += 1
        elif G[i][j] == 'L' and j != 0:
            j -= 1
        elif G[i][j] == 'R' and j != W-1:
            j += 1
        else:
            break
        if visited[i][j] == 1:
            print(-1)
            return
        visited[i][j] = 1
    print(i+1,j+1)

=======
Suggestion 5

def move(x,y,grid):
    if grid[x][y] == 'U' and x != 0:
        x -= 1
    elif grid[x][y] == 'D' and x != H - 1:
        x += 1
    elif grid[x][y] == 'L' and y != 0:
        y -= 1
    elif grid[x][y] == 'R' and y != W - 1:
        y += 1
    else:
        return -1
    return x, y

H, W = map(int, input().split())
grid = [input() for _ in range(H)]
x, y = 0, 0
visited = set()
while True:
    if (x, y) in visited:
        print(-1)
        break
    visited.add((x, y))
    res = move(x, y, grid)
    if res == -1:
        print(x + 1, y + 1)
        break
    else:
        x, y = res

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    g = [list(input()) for _ in range(h)]
    i,j = 0,0
    while True:
        if g[i][j] == "U":
            if i == 0:
                print(i+1,j+1)
                return
            else:
                i -= 1
        elif g[i][j] == "D":
            if i == h-1:
                print(i+1,j+1)
                return
            else:
                i += 1
        elif g[i][j] == "L":
            if j == 0:
                print(i+1,j+1)
                return
            else:
                j -= 1
        elif g[i][j] == "R":
            if j == w-1:
                print(i+1,j+1)
                return
            else:
                j += 1
        else:
            print(i+1,j+1)
            return
    print(-1)

=======
Suggestion 7

def main():
    # H, W = map(int, input().split())
    H, W = 9, 44
    # grid = [list(input()) for _ in range(H)]
    grid = [['R','R','D','D','D','D','R','R','R','D','D','D','R','R','R','R','R','R','D','D','D','R','D','D','D','D','R','D','D','D','D','D','D','R','D','D','R','D','D','D','D','D','R','D','R'],
            ['R','R','R','D','L','R','D','R','D','L','L','L','R','D','R','R','D','L','L','L','D','D','R','D','L','L','L','D','D','L','L','L','R','D','D','R','D','L','L','L','L','R','D','D'],
            ['D','R','D','L','R','L','D','R','D','L','R','L','D','R','L','D','R','D','L','D','D','L','R','D','L','D','D','L','R','D','L','R','L','D','R','D','L','R','L','D','R','R','R','D'],
            ['D','D','L','R','R','D','L','R','D','L','R','L','D','D','L','L','D','R','D','L','L','D','D','R','D','L','L','D','D','R','D','R','D','D','R','R','L','D','R','D','D','R','D','D'],
            ['R','D','L','R','R','D','L','R','D','L','L','L','L','R','D','L','R','D','R','R','D','D','D','L','L','L','L','L','L','D','R','D','R','R','D','L','D','D','D','L','L','L','R','D'],
            ['R','D','

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    i, j = 0, 0
    while True:
        if g[i][j] == "U" and i != 0:
            i -= 1
        elif g[i][j] == "D" and i != h - 1:
            i += 1
        elif g[i][j] == "L" and j != 0:
            j -= 1
        elif g[i][j] == "R" and j != w - 1:
            j += 1
        else:
            break
    if i == 0 and j == 0:
        print(-1)
    else:
        print(i + 1, j + 1)

=======
Suggestion 9

def solve():
    pass

=======
Suggestion 10

def main():
    pass
