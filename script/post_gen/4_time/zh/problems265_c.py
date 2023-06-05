Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    i = j = 0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                print(i+1, j+1)
                break
            else:
                i += 1
        elif G[i][j] == 'L':
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                print(i+1, j+1)
                break
            else:
                j += 1
        else:
            print(-1)
            break

=======
Suggestion 2

def main():
    H,W = map(int,input().split())
    G = []
    for i in range(H):
        G.append(input())
    x,y = 0,0
    for i in range(H*W):
        if G[x][y] == 'U':
            if x != 0:
                x -= 1
            else:
                print(-1)
                return
        elif G[x][y] == 'D':
            if x != H-1:
                x += 1
            else:
                print(-1)
                return
        elif G[x][y] == 'L':
            if y != 0:
                y -= 1
            else:
                print(-1)
                return
        elif G[x][y] == 'R':
            if y != W-1:
                y += 1
            else:
                print(-1)
                return
    print(x+1,y+1)

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    visited = [[False] * W for _ in range(H)]
    while 0 <= i < H and 0 <= j < W:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if G[i][j] == 'U':
            i -= 1
        elif G[i][j] == 'D':
            i += 1
        elif G[i][j] == 'L':
            j -= 1
        elif G[i][j] == 'R':
            j += 1
    print(i + 1, j + 1)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]
    x, y = 0, 0
    while True:
        if g[x][y] == 'U':
            if x == 0:
                break
            x -= 1
        elif g[x][y] == 'D':
            if x == h - 1:
                break
            x += 1
        elif g[x][y] == 'L':
            if y == 0:
                break
            y -= 1
        elif g[x][y] == 'R':
            if y == w - 1:
                break
            y += 1
    print(x + 1, y + 1)

=======
Suggestion 6

def move(x,y):
    if x<=0 or x>h or y<=0 or y>w:
        return False
    if grid[x-1][y-1] == 'U':
        x -= 1
    elif grid[x-1][y-1] == 'D':
        x += 1
    elif grid[x-1][y-1] == 'L':
        y -= 1
    elif grid[x-1][y-1] == 'R':
        y += 1
    else:
        return False
    return x,y

h,w = map(int,input().split())
grid = []
for i in range(h):
    grid.append(list(input()))
x,y = 1,1
visited = [[0 for i in range(w)] for j in range(h)]
while True:
    if visited[x-1][y-1] == 1:
        print(-1)
        break
    visited[x-1][y-1] = 1
    x,y = move(x,y)
    if x == False:
        print(x,y)
        break

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    g = [input() for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    x,y = 0,0
    while 0 <= x < h and 0 <= y < w and not visited[x][y]:
        visited[x][y] = 1
        if g[x][y] == "U":
            x -= 1
        elif g[x][y] == "D":
            x += 1
        elif g[x][y] == "L":
            y -= 1
        elif g[x][y] == "R":
            y += 1
    if 0 <= x < h and 0 <= y < w:
        print(x+1,y+1)
    else:
        print(-1)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                break
            i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                break
            i += 1
        elif G[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                break
            j += 1
    if i == 0 and j == 0:
        print(-1)
    else:
        print(i+1, j+1)

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    def dfs(x, y):
        if x < 0 or x >= h or y < 0 or y >= w:
            return (x, y)
        if visited[x][y]:
            return (-1, -1)
        visited[x][y] = True
        if g[x][y] == 'U':
            return dfs(x - 1, y)
        elif g[x][y] == 'D':
            return dfs(x + 1, y)
        elif g[x][y] == 'L':
            return dfs(x, y - 1)
        elif g[x][y] == 'R':
            return dfs(x, y + 1)
        else:
            return (-1, -1)
    print(dfs(0, 0)[0] + 1, dfs(0, 0)[1] + 1)

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    i = 0
    j = 0
    while True:
        if S[i][j] == 'U':
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i -= 1
        elif S[i][j] == 'D':
            if i == H-1:
                print(i+1, j+1)
                break
            else:
                i += 1
        elif S[i][j] == 'L':
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j -= 1
        elif S[i][j] == 'R':
            if j == W-1:
                print(i+1, j+1)
                break
            else:
                j += 1
        else:
            print(-1)
            break
