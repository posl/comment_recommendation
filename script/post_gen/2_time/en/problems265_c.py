Synthesizing 10/10 solutions

=======
Suggestion 1

def move(position, direction):
    if direction == 'U':
        position[0] -= 1
    elif direction == 'D':
        position[0] += 1
    elif direction == 'L':
        position[1] -= 1
    elif direction == 'R':
        position[1] += 1
    return position

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    i, j = 0, 0
    while True:
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
        if i < 0 or i >= H or j < 0 or j >= W:
            print(i + 1, j + 1)
            return

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    visited[0][0] = 1
    i = j = 0
    while True:
        if grid[i][j] == 'U':
            i -= 1
        elif grid[i][j] == 'D':
            i += 1
        elif grid[i][j] == 'L':
            j -= 1
        elif grid[i][j] == 'R':
            j += 1
        if i < 0 or i >= h or j < 0 or j >= w:
            print(i+1, j+1)
            return
        if visited[i][j] == 1:
            print(-1)
            return
        visited[i][j] = 1

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    grid = [input() for i in range(h)]
    visited = [[False] * w for i in range(h)]
    visited[0][0] = True
    i = 0
    j = 0
    while True:
        if grid[i][j] == 'U' and i != 0:
            i -= 1
        elif grid[i][j] == 'D' and i != h-1:
            i += 1
        elif grid[i][j] == 'L' and j != 0:
            j -= 1
        elif grid[i][j] == 'R' and j != w-1:
            j += 1
        else:
            break
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
    print(i+1, j+1)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    g = [[c for c in input()] for _ in range(h)]
    i, j = 0, 0
    for _ in range(h*w):
        if g[i][j] == 'U':
            if i == 0:
                break
            i -= 1
        elif g[i][j] == 'D':
            if i == h-1:
                break
            i += 1
        elif g[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        elif g[i][j] == 'R':
            if j == w-1:
                break
            j += 1
    else:
        print(-1)
        return
    print(i+1, j+1)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    x, y = 0, 0
    for _ in range(10**6):
        if G[x][y] == 'U':
            x -= 1
        elif G[x][y] == 'D':
            x += 1
        elif G[x][y] == 'L':
            y -= 1
        elif G[x][y] == 'R':
            y += 1
        if x < 0 or H-1 < x or y < 0 or W-1 < y:
            print(x+1, y+1)
            return
    print(-1)

main()

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    pos = [1, 1]
    visited = [[False for _ in range(W)] for _ in range(H)]
    while True:
        visited[pos[0]-1][pos[1]-1] = True
        if G[pos[0]-1][pos[1]-1] == "U":
            if pos[0] == 1:
                break
            else:
                pos[0] -= 1
        elif G[pos[0]-1][pos[1]-1] == "D":
            if pos[0] == H:
                break
            else:
                pos[0] += 1
        elif G[pos[0]-1][pos[1]-1] == "L":
            if pos[1] == 1:
                break
            else:
                pos[1] -= 1
        elif G[pos[0]-1][pos[1]-1] == "R":
            if pos[1] == W:
                break
            else:
                pos[1] += 1
        if visited[pos[0]-1][pos[1]-1] == True:
            pos = [-1, -1]
            break
    print(" ".join(map(str, pos)))

=======
Suggestion 8

def main():
    H,W = map(int,input().split())
    grid = [list(input()) for _ in range(H)]
    visited = [[False]*W for _ in range(H)]
    i = j = 0
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if grid[i][j] == 'U':
            if i == 0:
                print(i+1,j+1)
                return
            else:
                i -= 1
        elif grid[i][j] == 'D':
            if i == H-1:
                print(i+1,j+1)
                return
            else:
                i += 1
        elif grid[i][j] == 'L':
            if j == 0:
                print(i+1,j+1)
                return
            else:
                j -= 1
        elif grid[i][j] == 'R':
            if j == W-1:
                print(i+1,j+1)
                return
            else:
                j += 1

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    # print(grid)
    visited = [[0]*W for _ in range(H)]
    # print(visited)
    x, y = 0, 0
    while True:
        if grid[x][y] == 'U':
            if x == 0:
                break
            x -= 1
        elif grid[x][y] == 'D':
            if x == H-1:
                break
            x += 1
        elif grid[x][y] == 'L':
            if y == 0:
                break
            y -= 1
        elif grid[x][y] == 'R':
            if y == W-1:
                break
            y += 1
        if visited[x][y] == 1:
            print(-1)
            return
        visited[x][y] = 1
    print(x+1, y+1)
    return

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(input())

    #print("H = {} W = {}".format(H, W))
    #print("G = {}".format(G))

    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[0][0] = True
    i = 0
    j = 0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                break
            i -= 1
        elif G[i][j] == 'D':
            if i == H - 1:
                break
            i += 1
        elif G[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        elif G[i][j] == 'R':
            if j == W - 1:
                break
            j += 1
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
    print("{} {}".format(i + 1, j + 1))
