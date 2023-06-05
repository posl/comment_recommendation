Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[-1] * W for _ in range(H)]
    q = []
    q.append([C_h, C_w])
    dist[C_h][C_w] = 0
    while len(q) > 0:
        h, w = q.pop(0)
        for dh, dw in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nh = h + dh
            nw = w + dw
            if nh < 0 or nw < 0 or nh >= H or nw >= W:
                continue
            if S[nh][nw] == '#':
                continue
            if dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                q.append([nh, nw])
    print(dist[D_h][D_w])

=======
Suggestion 3

def main():
    h,w = map(int, input().split())
    c_h,c_w = map(int, input().split())
    d_h,d_w = map(int, input().split())
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    s = []
    for i in range(h):
        s.append(input())
    # print(s)
    ans = [[-1 for i in range(w)] for j in range(h)]
    ans[c_h][c_w] = 0
    # print(ans)
    q = [[c_h,c_w]]
    while len(q) > 0:
        # print(q)
        h,w = q.pop(0)
        # print(h,w)
        for i in range(-2,3):
            for j in range(-2,3):
                if abs(i) + abs(j) == 4:
                    continue
                if h+i < 0 or h+i >= len(s) or w+j < 0 or w+j >= len(s[0]):
                    continue
                if s[h+i][w+j] == '#':
                    continue
                if ans[h+i][w+j] == -1:
                    ans[h+i][w+j] = ans[h][w] + 1
                    q.append([h+i,w+j])
    print(ans[d_h][d_w])
main()

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    c_h,c_w = map(int,input().split())
    d_h,d_w = map(int,input().split())
    s = []
    for i in range(h):
        s.append(input())
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    #print(h,w,c_h,c_w,d_h,d_w,s)
    #print(s[0][0])
    #print(s[0][1])
    #print(s[1][0])
    #print(s[1][1])
    #print(s[1][2])
    #print(s[2][1])
    #print(s[2][2])
    #print(s[2][3])
    #print(s[3][2])
    #print(s[3][3])
    #print(s[3][4])
    #print(s[4][3])
    #print(s[4][4])
    #print(s[4][5])
    #print(s[5][4])
    #print(s[5][5])
    #print(s[5][6])
    #print(s[6][5])
    #print(s[6][6])
    #print(s[6][7])
    #print(s[7][6])
    #print(s[7][7])
    #print(s[7][8])
    #print(s[8][7])
    #print(s[8][8])
    #print(s[8][9])
    #print(s[9][8])
    #print(s[9][9])
    #print(s[9][10])
    #print(s[10][9])
    #print(s[10][10])
    #print(s[10][11])
    #print(s[11][10])
    #print(s[11][11])
    #print(s[11][12])
    #print(s[12][11])
    #print(s[12][12])
    #print(s[12][13])
    #print(s[13][12])
    #print(s[13][13])
    #print(s[13][14])
    #print(s[14][13])
    #print(s[14][14])
    #print(s[14][15])
    #print(s[15][14])

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    s = [input() for _ in range(h)]

    # 距离を管理する配列
    dist = [[-1] * w for _ in range(h)]

    # 幅優先探索
    q = []
    q.append((c_h - 1, c_w - 1))
    dist[c_h - 1][c_w - 1] = 0
    while len(q) > 0:
        i, j = q.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
            if not (0 <= i2 < h and 0 <= j2 < w):
                continue
            if s[i2][j2] == '#':
                continue
            if dist[i2][j2] == -1:
                dist[i2][j2] = dist[i][j] + 1
                q.append((i2, j2))

    # 答え
    ans = dist[d_h - 1][d_w - 1]
    print(ans)

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    s = [input() for _ in range(h)]
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    dist = [[float('inf')] * w for _ in range(h)]
    dist[c_h][c_w] = 0
    queue = [(c_h, c_w)]
    while queue:
        i, j = queue.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if not (0 <= i2 < h and 0 <= j2 < w): continue
            if s[i2][j2] == '#': continue
            if dist[i2][j2] <= dist[i][j]: continue
            dist[i2][j2] = dist[i][j]
            queue.append((i2, j2))
        for i2 in range(i - 2, i + 3):
            for j2 in range(j - 2, j + 3):
                if not (0 <= i2 < h and 0 <= j2 < w): continue
                if s[i2][j2] == '#': continue
                if dist[i2][j2] <= dist[i][j] + 1: continue
                dist[i2][j2] = dist[i][j] + 1
                queue.append((i2, j2))
    if dist[d_h][d_w] == float('inf'):
        print(-1)
    else:
        print(dist[d_h][d_w])

=======
Suggestion 8

def dfs(x,y):
    if x == d_h and y == d_w:
        return 0
    if visited[x][y]:
        return float('inf')
    visited[x][y] = True
    res = float('inf')
    for dx in range(-2,3):
        for dy in range(-2,3):
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.':
                res = min(res,dfs(nx,ny) + 1)
    visited[x][y] = False
    return res

h,w = map(int,input().split())
c_h,c_w = map(int,input().split())
d_h,d_w = map(int,input().split())
c_h -= 1
c_w -= 1
d_h -= 1
d_w -= 1
s = []
for i in range(h):
    s.append(input())
visited = [[False] * w for _ in range(h)]
ans = dfs(c_h,c_w)
