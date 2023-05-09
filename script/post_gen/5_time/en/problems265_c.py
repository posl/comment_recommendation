Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    G = [list(input()) for _ in range(H)]
    i, j = 0, 0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                print(i+1, j+1)
                return
            else:
                i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                print(i+1, j+1)
                return
            else:
                i += 1
        elif G[i][j] == 'L':
            if j == 0:
                print(i+1, j+1)
                return
            else:
                j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                print(i+1, j+1)
                return
            else:
                j += 1

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    while True:
        if G[i][j] == 'R' and j != W-1:
            j += 1
        elif G[i][j] == 'D' and i != H-1:
            i += 1
        elif G[i][j] == 'L' and j != 0:
            j -= 1
        elif G[i][j] == 'U' and i != 0:
            i -= 1
        else:
            break
    print(i+1, j+1)

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    G = []
    for i in range(H):
        G.append(input())
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
    if i == 0 and j == 0:
        print(-1)
    else:
        print(i+1, j+1)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i, j = 0, 0
    while True:
        if i < 0 or i >= H or j < 0 or j >= W:
            print(i + 1, j + 1)
            return
        if G[i][j] == 'U':
            i -= 1
        elif G[i][j] == 'D':
            i += 1
        elif G[i][j] == 'L':
            j -= 1
        elif G[i][j] == 'R':
            j += 1
        else:
            print(i + 1, j + 1)
            return

main()

=======
Suggestion 5

def main():
    H,W = map(int, input().split())
    G = [input() for _ in range(H)]
    i,j = 0,0
    while True:
        if G[i][j] == 'U':
            if i == 0:
                break
            else:
                i -= 1
        elif G[i][j] == 'D':
            if i == H-1:
                break
            else:
                i += 1
        elif G[i][j] == 'L':
            if j == 0:
                break
            else:
                j -= 1
        elif G[i][j] == 'R':
            if j == W-1:
                break
            else:
                j += 1
        else:
            break
    print(i+1, j+1)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    g = [input() for _ in range(h)]
    i, j = 0, 0
    while 1:
        g[i] = g[i][:j] + 'x' + g[i][j+1:]
        if g[i][j] == 'x':
            print(-1)
            break
        elif g[i][j] == 'U':
            i -= 1
        elif g[i][j] == 'D':
            i += 1
        elif g[i][j] == 'L':
            j -= 1
        elif g[i][j] == 'R':
            j += 1
        if i < 0 or i >= h or j < 0 or j >= w:
            print(i+1, j+1)
            break
main()

=======
Suggestion 7

def main():
    h,w = map(int,input().split())
    g = [list(input()) for i in range(h)]
    x,y = 0,0
    while True:
        if g[x][y] == 'R':
            if y == w-1:
                print(x+1,y+1)
                break
            else:
                y += 1
        elif g[x][y] == 'L':
            if y == 0:
                print(x+1,y+1)
                break
            else:
                y -= 1
        elif g[x][y] == 'U':
            if x == 0:
                print(x+1,y+1)
                break
            else:
                x -= 1
        elif g[x][y] == 'D':
            if x == h-1:
                print(x+1,y+1)
                break
            else:
                x += 1
        else:
            print(x+1,y+1)
            break

=======
Suggestion 8

def solve():
    h,w = map(int,input().split())
    g = []
    for i in range(h):
        g.append(input())
    i,j = 0,0
    while True:
        if g[i][j] == "R":
            if j == w-1:
                print(i+1,j+1)
                return
            j += 1
        elif g[i][j] == "L":
            if j == 0:
                print(i+1,j+1)
                return
            j -= 1
        elif g[i][j] == "U":
            if i == 0:
                print(i+1,j+1)
                return
            i -= 1
        elif g[i][j] == "D":
            if i == h-1:
                print(i+1,j+1)
                return
            i += 1
        else:
            print(-1)
            return

=======
Suggestion 9

def solve():
    # Implement solution here
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    i, j = 0, 0
    while True:
        if grid[i][j] == "U":
            if i == 0:
                print(i+1, j+1)
                return
            else:
                i -= 1
        elif grid[i][j] == "D":
            if i == h-1:
                print(i+1, j+1)
                return
            else:
                i += 1
        elif grid[i][j] == "L":
            if j == 0:
                print(i+1, j+1)
                return
            else:
                j -= 1
        elif grid[i][j] == "R":
            if j == w-1:
                print(i+1, j+1)
                return
            else:
                j += 1

=======
Suggestion 10

def main():
    # Write code here
    H,W = map(int,input().split())
    G = [list(input()) for i in range(H)]
    x,y = 0,0
    while True:
        if G[x][y] == 'U':
            x -= 1
        elif G[x][y] == 'D':
            x += 1
        elif G[x][y] == 'L':
            y -= 1
        else:
            y += 1
        if x < 0 or x >= H or y < 0 or y >= W:
            print(x+1,y+1)
            break
