Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]

    visited = [[False] * W for _ in range(H)]
    i, j = 0, 0
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
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
    print(i + 1, j + 1)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    i, j = 0, 0
    for _ in range(H*W):
        if grid[i][j] == 'U':
            i -= 1
        elif grid[i][j] == 'D':
            i += 1
        elif grid[i][j] == 'L':
            j -= 1
        elif grid[i][j] == 'R':
            j += 1
        if i < 0 or i >= H or j < 0 or j >= W:
            print(i+1, j+1)
            return
    print(-1)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            grid[i][j] = [i, j]
    i, j = 0, 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    while True:
        if visited[i][j]:
            print(-1)
            return
        visited[i][j] = True
        if grid[i][j] == "U":
            if i == 0:
                print(*grid[i][j])
                return
            i -= 1
        elif grid[i][j] == "D":
            if i == h - 1:
                print(*grid[i][j])
                return
            i += 1
        elif grid[i][j] == "L":
            if j == 0:
                print(*grid[i][j])
                return
            j -= 1
        elif grid[i][j] == "R":
            if j == w - 1:
                print(*grid[i][j])
                return
            j += 1
        else:
            print("error")
            return

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    g = [list(input()) for i in range(h)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i = 0
    j = 0
    for k in range(1000000):
        if i == h-1 and j == w-1:
            print(i+1, j+1)
            return
        if g[i][j] == 'U':
            i += di[0]
            j += dj[0]
        elif g[i][j] == 'D':
            i += di[1]
            j += dj[1]
        elif g[i][j] == 'L':
            i += di[2]
            j += dj[2]
        elif g[i][j] == 'R':
            i += di[3]
            j += dj[3]
    print(-1)

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]
    x, y = 0, 0
    for i in range(10**6):
        if x == h-1 and y == w-1:
            print(x+1, y+1)
            return
        if g[x][y] == "U":
            if x == 0:
                print(-1)
                return
            x -= 1
        elif g[x][y] == "D":
            if x == h-1:
                print(-1)
                return
            x += 1
        elif g[x][y] == "L":
            if y == 0:
                print(-1)
                return
            y -= 1
        elif g[x][y] == "R":
            if y == w-1:
                print(-1)
                return
            y += 1
    print(-1)
    return

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    G = []
    for i in range(H):
        G.append(list(input()))
    now = [0, 0]
    while True:
        if G[now[0]][now[1]] == "U":
            if now[0] == 0:
                print(" ".join(map(str, [now[0]+1, now[1]+1])))
                break
            else:
                now[0] -= 1
        elif G[now[0]][now[1]] == "D":
            if now[0] == H-1:
                print(" ".join(map(str, [now[0]+1, now[1]+1])))
                break
            else:
                now[0] += 1
        elif G[now[0]][now[1]] == "L":
            if now[1] == 0:
                print(" ".join(map(str, [now[0]+1, now[1]+1])))
                break
            else:
                now[1] -= 1
        elif G[now[0]][now[1]] == "R":
            if now[1] == W-1:
                print(" ".join(map(str, [now[0]+1, now[1]+1])))
                break
            else:
                now[1] += 1
        else:
            print(-1)
            break

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    ans = [1, 1]
    for i in range(H*W):
        if G[ans[0]-1][ans[1]-1] == "U":
            ans[0] -= 1
        elif G[ans[0]-1][ans[1]-1] == "D":
            ans[0] += 1
        elif G[ans[0]-1][ans[1]-1] == "L":
            ans[1] -= 1
        elif G[ans[0]-1][ans[1]-1] == "R":
            ans[1] += 1
        if ans[0] == 0 or ans[0] == H+1 or ans[1] == 0 or ans[1] == W+1:
            break
    if ans[0] == 0 or ans[0] == H+1 or ans[1] == 0 or ans[1] == W+1:
        print(" ".join(map(str, ans)))
    else:
        print(-1)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(input())
    #print(grid)
    i = 0
    j = 0
    for _ in range(H*W):
        if grid[i][j] == "U":
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i = i-1
        elif grid[i][j] == "D":
            if i == H-1:
                print(i+1, j+1)
                break
            else:
                i = i+1
        elif grid[i][j] == "L":
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j = j-1
        elif grid[i][j] == "R":
            if j == W-1:
                print(i+1, j+1)
                break
            else:
                j = j+1
        else:
            print(-1)
            break
    else:
        print(-1)

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    #print(H, W)
    #print(G)
    
    # 0:上 1:右 2:下 3:左
    # dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    # 0:右 1:下 2:左 3:上
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    # 0:右 1:下 2:左 3:上
    d = 0
    x, y = 0, 0
    for i in range(10000000):
        #print(x, y)
        if x == W-1 and y == H-1:
            print(y+1, x+1)
            return
        if G[y][x] == "U":
            d = 3
        elif G[y][x] == "D":
            d = 1
        elif G[y][x] == "L":
            d = 2
        elif G[y][x] == "R":
            d = 0
        else:
            print("error")
            return
        x = x + dx[d]
        y = y + dy[d]
        if x < 0 or x >= W or y < 0 or y >= H:
            print(-1)
            return
    print(-1)
    return

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)] # 2次元配列を入力するときはこのようにしておくと便利
    i = 0
    j = 0
    for _ in range(H*W):
        if G[i][j] == "U":
            if i != 0:
                i -= 1
            else:
                print(i+1, j+1)
                return
        elif G[i][j] == "D":
            if i != H-1:
                i += 1
            else:
                print(i+1, j+1)
                return
        elif G[i][j] == "L":
            if j != 0:
                j -= 1
            else:
                print(i+1, j+1)
                return
        elif G[i][j] == "R":
            if j != W-1:
                j += 1
            else:
                print(i+1, j+1)
                return
    print(-1)
