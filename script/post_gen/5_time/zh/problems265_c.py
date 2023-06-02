Synthesizing 10/10 solutions

=======
Suggestion 1

def problem265_c():
    pass

=======
Suggestion 2

def problems265_c():
    pass

=======
Suggestion 3

def get_input():
    h, w = map(int, input().split())
    g = []
    for i in range(h):
        g.append(input())
    return h, w, g

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    i = 0
    j = 0
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
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    x, y = 0, 0
    visited = [[0 for _ in range(W)] for _ in range(H)]
    while True:
        if grid[x][y] == 'U':
            if x == 0:
                break
            else:
                x -= 1
        elif grid[x][y] == 'D':
            if x == H - 1:
                break
            else:
                x += 1
        elif grid[x][y] == 'L':
            if y == 0:
                break
            else:
                y -= 1
        elif grid[x][y] == 'R':
            if y == W - 1:
                break
            else:
                y += 1
        if visited[x][y] == 1:
            print(-1)
            return
        else:
            visited[x][y] = 1
    print(x + 1, y + 1)
    return

main()

=======
Suggestion 7

def problem265_c():
    return None

=======
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    H,W = map(int,input().split())
    G = [[0 for i in range(W+2)] for j in range(H+2)]
    for i in range(1,H+1):
        G[i] = [0] + list(input()) + [0]
    x = 1
    y = 1
    while True:
        if G[x][y] == 'U':
            x -= 1
        elif G[x][y] == 'D':
            x += 1
        elif G[x][y] == 'L':
            y -= 1
        elif G[x][y] == 'R':
            y += 1
        if x == 0 or x == H+1 or y == 0 or y == W+1:
            break
    if x == 0:
        x += 1
    elif x == H+1:
        x -= 1
    elif y == 0:
        y += 1
    elif y == W+1:
        y -= 1
    print(x,y)

=======
Suggestion 10

def move(i,j):
    if G[i-1][j-1] == "U" and i!=1:
        return i-1,j
    elif G[i-1][j-1] == "D" and i!=H:
        return i+1,j
    elif G[i-1][j-1] == "L" and j!=1:
        return i,j-1
    elif G[i-1][j-1] == "R" and j!=W:
        return i,j+1
    else:
        return -1,-1

H,W = map(int,input().split())
G = [list(input()) for i in range(H)]
i,j = 1,1
seen = [[0 for i in range(W)] for j in range(H)]
seen[0][0] = 1
while True:
    i,j = move(i,j)
    if i==-1 and j==-1:
        print(-1)
        break
    elif seen[i-1][j-1] == 1:
        print(i,j)
        break
    else:
        seen[i-1][j-1] = 1
