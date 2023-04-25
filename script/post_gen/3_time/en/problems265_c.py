Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    i, j = 0, 0
    while True:
        if i < 0 or i >= H or j < 0 or j >= W:
            print(-1)
            return
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

main()

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    for _ in range(H * W):
        if G[i][j] == 'U':
            i -= 1
        elif G[i][j] == 'D':
            i += 1
        elif G[i][j] == 'L':
            j -= 1
        else:
            j += 1
        if i < 0 or i >= H or j < 0 or j >= W:
            print(i + 1, j + 1)
            return
    print(-1)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    i, j = 0, 0
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if grid[i][j] == "U":
            if i == 0:
                print(i + 1, j + 1)
                return
            i -= 1
        elif grid[i][j] == "D":
            if i == h - 1:
                print(i + 1, j + 1)
                return
            i += 1
        elif grid[i][j] == "L":
            if j == 0:
                print(i + 1, j + 1)
                return
            j -= 1
        elif grid[i][j] == "R":
            if j == w - 1:
                print(i + 1, j + 1)
                return
            j += 1

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    i, j = 0, 0
    for _ in range(H * W):
        if G[i][j] == "U":
            if i == 0:
                print(i + 1, j + 1)
                break
            else:
                i -= 1
        elif G[i][j] == "D":
            if i == H - 1:
                print(i + 1, j + 1)
                break
            else:
                i += 1
        elif G[i][j] == "L":
            if j == 0:
                print(i + 1, j + 1)
                break
            else:
                j -= 1
        elif G[i][j] == "R":
            if j == W - 1:
                print(i + 1, j + 1)
                break
            else:
                j += 1
    else:
        print(-1)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    i, j = 0, 0
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if grid[i][j] == 'U':
            if i > 0:
                i -= 1
            else:
                break
        elif grid[i][j] == 'D':
            if i < h - 1:
                i += 1
            else:
                break
        elif grid[i][j] == 'L':
            if j > 0:
                j -= 1
            else:
                break
        elif grid[i][j] == 'R':
            if j < w - 1:
                j += 1
            else:
                break
    print(i + 1, j + 1)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]
    i, j = 0, 0
    for _ in range(h * w):
        if g[i][j] == "U":
            i -= 1
        elif g[i][j] == "D":
            i += 1
        elif g[i][j] == "L":
            j -= 1
        elif g[i][j] == "R":
            j += 1
        if i < 0 or i >= h or j < 0 or j >= w:
            print(i + 1, j + 1)
            break
    else:
        print(-1)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    visited = [[False for j in range(w)] for i in range(h)]
    i = 0
    j = 0
    while True:
        visited[i][j] = True
        if grid[i][j] == "U":
            i -= 1
        elif grid[i][j] == "D":
            i += 1
        elif grid[i][j] == "L":
            j -= 1
        elif grid[i][j] == "R":
            j += 1
        else:
            print("Error")
            return
        if i < 0 or i >= h or j < 0 or j >= w:
            print(i+1, j+1)
            return
        if visited[i][j]:
            print(-1)
            return

main()

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(list(input()))
    visited = [[False for i in range(W)] for j in range(H)]
    i = 0
    j = 0
    while True:
        if i < 0 or i >= H or j < 0 or j >= W:
            print(-1)
            return
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if grid[i][j] == 'U':
            i -= 1
        elif grid[i][j] == 'D':
            i += 1
        elif grid[i][j] == 'L':
            j -= 1
        elif grid[i][j] == 'R':
            j += 1
    print(i+1, j+1)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    #print(grid)
    #print(H, W)
    x, y = 0, 0
    #print(x, y)
    count = 0
    while True:
        if count > H * W:
            print(-1)
            break
        if grid[x][y] == "U":
            if x == 0:
                print(x+1, y+1)
                break
            else:
                x -= 1
        elif grid[x][y] == "D":
            if x == H-1:
                print(x+1, y+1)
                break
            else:
                x += 1
        elif grid[x][y] == "L":
            if y == 0:
                print(x+1, y+1)
                break
            else:
                y -= 1
        elif grid[x][y] == "R":
            if y == W-1:
                print(x+1, y+1)
                break
            else:
                y += 1
        count += 1

main()

=======
Suggestion 10

def main():
    H,W=map(int,input().split())
    G=[input() for _ in range(H)]
    d=[(0,1),(1,0),(0,-1),(-1,0)]
    v=[[-1]*W for _ in range(H)]
    v[0][0]=0
    i,j=0,0
    while True:
        if G[i][j]=='U':
            i-=1
        elif G[i][j]=='D':
            i+=1
        elif G[i][j]=='L':
            j-=1
        elif G[i][j]=='R':
            j+=1
        if i<0 or i>=H or j<0 or j>=W:
            break
        if v[i][j]>=0:
            print(-1)
            exit()
        v[i][j]=0
    print(i+1,j+1)
