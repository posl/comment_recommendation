Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i = 0
    j = 0
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
    print(i+1, j+1)

=======
Suggestion 2

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
            if i == H - 1:
                break
            i += 1
        elif G[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        else:
            if j == W - 1:
                break
            j += 1
    print(i + 1, j + 1)

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]
    i = j = 0
    while True:
        if g[i][j] == 'U':
            if i == 0:
                break
            i -= 1
        elif g[i][j] == 'D':
            if i == h - 1:
                break
            i += 1
        elif g[i][j] == 'L':
            if j == 0:
                break
            j -= 1
        else:
            if j == w - 1:
                break
            j += 1
    print(i + 1, j + 1)

=======
Suggestion 4

def main():
    h, w = map(int, input().split())
    g = [list(input()) for _ in range(h)]
    x, y = 0, 0
    while True:
        g[x][y] = '.'
        if g[x][y] == 'U':
            if x == 0:
                print(x+1, y+1)
                return
            x -= 1
        elif g[x][y] == 'D':
            if x == h-1:
                print(x+1, y+1)
                return
            x += 1
        elif g[x][y] == 'L':
            if y == 0:
                print(x+1, y+1)
                return
            y -= 1
        elif g[x][y] == 'R':
            if y == w-1:
                print(x+1, y+1)
                return
            y += 1
        else:
            print(x+1, y+1)
            return
        if g[x][y] == '.':
            print(-1)
            return

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    G = [list(input()) for i in range(H)]
    i = 0
    j = 0
    while True:
        if G[i][j] == 'U':
            if i != 0:
                i -= 1
            else:
                break
        elif G[i][j] == 'D':
            if i != H-1:
                i += 1
            else:
                break
        elif G[i][j] == 'L':
            if j != 0:
                j -= 1
            else:
                break
        elif G[i][j] == 'R':
            if j != W-1:
                j += 1
            else:
                break
        else:
            break
    if G[i][j] == '.':
        print(i+1,j+1)
    else:
        print(-1)

=======
Suggestion 6

def main():
    h,w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    i = 0
    j = 0
    while True:
        if g[i][j] == 'U':
            if i != 0:
                i = i - 1
            else:
                print(i+1, j+1)
                break
        elif g[i][j] == 'D':
            if i != h-1:
                i = i + 1
            else:
                print(i+1, j+1)
                break
        elif g[i][j] == 'L':
            if j != 0:
                j = j - 1
            else:
                print(i+1, j+1)
                break
        elif g[i][j] == 'R':
            if j != w-1:
                j = j + 1
            else:
                print(i+1, j+1)
                break
        else:
            print(-1)
            break

=======
Suggestion 7

def main():
    h,w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    i,j = 0,0
    while True:
        if g[i][j] == 'U':
            if i == 0:
                break
            else:
                i-=1
        elif g[i][j] == 'D':
            if i == h-1:
                break
            else:
                i+=1
        elif g[i][j] == 'L':
            if j == 0:
                break
            else:
                j-=1
        elif g[i][j] == 'R':
            if j == w-1:
                break
            else:
                j+=1
        else:
            break
    print(i+1,j+1)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]

    # print(H, W)
    # print(G)

    i = 0
    j = 0
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

    print(i+1, j+1)

main()

=======
Suggestion 9

def main():
    H,W = map(int, input().split())
    G = []
    for i in range(H):
        G.append(input())
    visited = [[False for _ in range(W)] for _ in range(H)]
    i,j = 0,0
    while True:
        if visited[i][j]:
            print(-1)
            break
        visited[i][j] = True
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

=======
Suggestion 10

def get_input():
    return input().split()
