Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                if i == 0 or i == H-1 or j == 0 or j == W-1:
                    print(4)
                    exit()
                if i > 0 and S[i-1][j] == ".":
                    ans += 1
                if i < H-1 and S[i+1][j] == ".":
                    ans += 1
                if j > 0 and S[i][j-1] == ".":
                    ans += 1
                if j < W-1 and S[i][j+1] == ".":
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                if i == 0:
                    print('4')
                    return
                if i == H-1:
                    print('4')
                    return
                if j == 0:
                    print('4')
                    return
                if j == W-1:
                    print('4')
                    return
                if i-1 >= 0:
                    if S[i-1][j] == '.':
                        print('4')
                        return
                if i+1 <= H-1:
                    if S[i+1][j] == '.':
                        print('4')
                        return
                if j-1 >= 0:
                    if S[i][j-1] == '.':
                        print('4')
                        return
                if j+1 <= W-1:
                    if S[i][j+1] == '.':
                        print('4')
                        return

    print('3')

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = 0
    for i in range(1, H-1):
        for j in range(1, W-1):
            if S[i][j] == '#':
                if S[i-1][j] == '.' or S[i+1][j] == '.' or S[i][j-1] == '.' or S[i][j+1] == '.':
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    black = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                black += 1
    if black == 1:
        print(1)
        return
    if black == H * W:
        print(H * W)
        return
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                if i == 0 or i == H - 1 or j == 0 or j == W - 1:
                    print(2)
                    return
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                if i == 1 or i == H - 2 or j == 1 or j == W - 2:
                    print(3)
                    return
    print(4)
    return

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    print(solve(H, W, S))

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    # 1. find the black squares
    black = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                black.append((i, j))

    # 2. make a graph
    graph = {}
    for i, j in black:
        graph[(i, j)] = []
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if (i + di, j + dj) in black:
                graph[(i, j)].append((i + di, j + dj))

    # 3. find the number of sides
    visited = set()
    def dfs(i, j):
        if (i, j) in visited:
            return
        visited.add((i, j))
        for di, dj in graph[(i, j)]:
            dfs(di, dj)

    dfs(black[0][0], black[0][1])
    if len(visited) == len(black):
        print(4)
    else:
        print(3)

=======
Suggestion 7

def main():
    #input
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    #print(s)

    #find the first black
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                start = [i, j]
                break
        else:
            continue
        break

    #find the next black
    def find_next_black(start, s):
        i = start[0]
        j = start[1]
        #print(i, j)
        if i > 0 and s[i-1][j] == "#":
            return [i-1, j]
        elif i < h-1 and s[i+1][j] == "#":
            return [i+1, j]
        elif j > 0 and s[i][j-1] == "#":
            return [i, j-1]
        else:
            return [i, j+1]

    #find the next black
    next = find_next_black(start, s)
    #print(next)

    #count the sides
    count = 1
    while next != start:
        next = find_next_black(next, s)
        #print(next)
        count += 1

    #output
    print(count)

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    #print(H, W)
    #print(S)
    #print()
    #print()

    #print("start")
    #print("S[0][0] = ", S[0][0])
    #print("S[0][1] = ", S[0][1])
    #print("S[0][2] = ", S[0][2])
    #print("S[0][3] = ", S[0][3])
    #print("S[0][4] = ", S[0][4])
    #print("S[1][0] = ", S[1][0])
    #print("S[1][1] = ", S[1][1])
    #print("S[1][2] = ", S[1][2])
    #print("S[1][3] = ", S[1][3])
    #print("S[1][4] = ", S[1][4])
    #print("S[2][0] = ", S[2][0])
    #print("S[2][1] = ", S[2][1])
    #print("S[2][2] = ", S[2][2])
    #print("S[2][3] = ", S[2][3])
    #print("S[2][4] = ", S[2][4])
    #print("S[3][0] = ", S[3][0])
    #print("S[3][1] = ", S[3][1])
    #print("S[3][2] = ", S[3][2])
    #print("S[3][3] = ", S[3][3])
    #print("S[3][4] = ", S[3][4])
    #print("S[4][0] = ", S[4][0])
    #print("S[4][1] = ", S[4][1])
    #print("S[4][2] = ", S[4][2])
    #print("S[4][3] = ", S[4][3])
    #print("S[4][4] = ", S[4][

=======
Suggestion 9

def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    #print(s)
    #print("h = ", h, "w = ", w)
    side = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "#":
                #print("i = ", i, "j = ", j)
                if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                    side = 4
                elif s[i - 1][j] == "#" or s[i + 1][j] == "#" or s[i][j - 1] == "#" or s[i][j + 1] == "#":
                    side = 4
                else:
                    side = 8
                    break
        if side == 8:
            break
    print(side)
main()

=======
Suggestion 10

def paint ( grid , x , y , color , visited ): # x, y is the current location # color is the color of the current location # visited is a set of visited locations # returns the number of sides of the polygon that has the current location as one of its vertices # if the current location is a black square, it returns 0 # if the current location is a white square, it returns 1 # if the current location is a black square and is adjacent to a white square, it returns 1 # if the current location is a white square and is adjacent to a black square, it returns 1 if grid [ y ][ x ] == '#' : return 0 if ( x , y ) in visited : return 0 visited . add (( x , y )) sides = 0 if x > 0 : sides += paint ( grid , x - 1 , y , color , visited ) if x < len ( grid [ y ]) - 1 : sides += paint ( grid , x + 1 , y , color , visited ) if y > 0 : sides += paint ( grid , x , y - 1 , color , visited ) if y < len ( grid ) - 1 : sides += paint ( grid , x , y + 1 , color , visited ) return sides
