Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    G = [list(input()) for i in range(H)]
    i = 0
    j = 0
    while True:
        if G[i][j] == "U":
            if i == 0:
                print(i + 1, j + 1)
                exit()
            else:
                i -= 1
        elif G[i][j] == "D":
            if i == H - 1:
                print(i + 1, j + 1)
                exit()
            else:
                i += 1
        elif G[i][j] == "L":
            if j == 0:
                print(i + 1, j + 1)
                exit()
            else:
                j -= 1
        elif G[i][j] == "R":
            if j == W - 1:
                print(i + 1, j + 1)
                exit()
            else:
                j += 1
        if i == 0 and j == 0:
            print(-1)
            exit()

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'U':
                if i == 0:
                    print(-1)
                    return
                else:
                    i -= 1
            elif grid[i][j] == 'D':
                if i == H - 1:
                    print(-1)
                    return
                else:
                    i += 1
            elif grid[i][j] == 'L':
                if j == 0:
                    print(-1)
                    return
                else:
                    j -= 1
            elif grid[i][j] == 'R':
                if j == W - 1:
                    print(-1)
                    return
                else:
                    j += 1
            if grid[i][j] == 'G':
                print(i+1, j+1)
                return

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    g = [list(input()) for i in range(h)]
    i = 0
    j = 0
    while True:
        if g[i][j] == "U":
            if i == 0:
                print(i+1, j+1)
                break
            else:
                i -= 1
        elif g[i][j] == "D":
            if i == h-1:
                print(i+1, j+1)
                break
            else:
                i += 1
        elif g[i][j] == "L":
            if j == 0:
                print(i+1, j+1)
                break
            else:
                j -= 1
        elif g[i][j] == "R":
            if j == w-1:
                print(i+1, j+1)
                break
            else:
                j += 1
        else:
            print(i+1, j+1)
            break
    return 0

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    x, y = 0, 0
    while True:
        if visited[x][y]:
            print(-1)
            break
        visited[x][y] = True
        if G[x][y] == 'U':
            if x == 0:
                print(x + 1, y + 1)
                break
            else:
                x -= 1
        elif G[x][y] == 'D':
            if x == H - 1:
                print(x + 1, y + 1)
                break
            else:
                x += 1
        elif G[x][y] == 'L':
            if y == 0:
                print(x + 1, y + 1)
                break
            else:
                y -= 1
        elif G[x][y] == 'R':
            if y == W - 1:
                print(x + 1, y + 1)
                break
            else:
                y += 1

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    i, j = 0, 0
    while (i, j) != (H - 1, W - 1):
        if G[i][j] == 'R':
            G[i][j] = '.'
            j += 1
            if j >= W:
                print(-1)
                return
        elif G[i][j] == 'D':
            G[i][j] = '.'
            i += 1
            if i >= H:
                print(-1)
                return
        elif G[i][j] == 'L':
            G[i][j] = '.'
            j -= 1
            if j < 0:
                print(-1)
                return
        elif G[i][j] == 'U':
            G[i][j] = '.'
            i -= 1
            if i < 0:
                print(-1)
                return
        else:
            print(-1)
            return
    print(i + 1, j + 1)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    x, y = 0, 0
    while True:
        if x == h or x == -1 or y == w or y == -1:
            print(x+1, y+1)
            break
        elif s[x][y] == "R":
            s[x][y] = "."
            y += 1
        elif s[x][y] == "L":
            s[x][y] = "."
            y -= 1
        elif s[x][y] == "U":
            s[x][y] = "."
            x -= 1
        elif s[x][y] == "D":
            s[x][y] = "."
            x += 1
        else:
            print(-1)
            break

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())

    x = 0
    y = 0
    for i in range(1000):
        if x == h-1 and y == w-1:
            break
        if g[x][y] == 'R':
            y += 1
        elif g[x][y] == 'L':
            y -= 1
        elif g[x][y] == 'U':
            x -= 1
        elif g[x][y] == 'D':
            x += 1
        else:
            print(-1)
            return
        if x < 0 or y < 0 or x >= h or y >= w:
            print(-1)
            return
    print(x+1, y+1)

=======
Suggestion 8

def main():
    H, W = list(map(int, input().split()))
    grid = [list(input()) for _ in range(H)]
    i, j = 0, 0
    for _ in range(H * W):
        if grid[i][j] == 'U':
            if i == 0:
                print(-1)
                exit()
            i -= 1
        elif grid[i][j] == 'D':
            if i == H - 1:
                print(-1)
                exit()
            i += 1
        elif grid[i][j] == 'L':
            if j == 0:
                print(-1)
                exit()
            j -= 1
        elif grid[i][j] == 'R':
            if j == W - 1:
                print(-1)
                exit()
            j += 1
        else:
            print('error')
            exit()
    print(i + 1, j + 1)

=======
Suggestion 9

def main():
    H,W = map(int, input().split())
    G = list()
    for i in range(H):
        G.append(list(input()))
    x,y = 0,0
    while True:
        if G[x][y] == 'R':
            if y == W-1:
                print(-1)
                exit()
            y += 1
        elif G[x][y] == 'L':
            if y == 0:
                print(-1)
                exit()
            y -= 1
        elif G[x][y] == 'U':
            if x == 0:
                print(-1)
                exit()
            x -= 1
        elif G[x][y] == 'D':
            if x == H-1:
                print(-1)
                exit()
            x += 1
        if x == 0 and y == 0:
            print(-1)
            exit()
        if x == H-1 and y == W-1:
            print(x+1,y+1)
            exit()

=======
Suggestion 10

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    #print(H, W)
    #print(G)
    ans = ''
    i = 0
    j = 0
    while True:
        #print(i, j)
        ans += G[i][j]
        if G[i][j] == 'U':
            if i == 0:
                print(-1)
                exit()
            else:
                i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                print(-1)
                exit()
            else:
                i += 1
        elif G[i][j] == 'L':
            if j == 0:
                print(-1)
                exit()
            else:
                j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                print(-1)
                exit()
            else:
                j += 1
        if ans.count(ans[-1]) >= 3:
            print(-1)
            exit()
        if i == 0 and j == 0:
            print(-1)
            exit()
        if ans[-2:] == 'UD' or ans[-2:] == 'DU' or ans[-2:] == 'LR' or ans[-2:] == 'RL':
            print(-1)
            exit()
        if i == H-1 and j == W-1:
            print(i+1, j+1)
            exit()
