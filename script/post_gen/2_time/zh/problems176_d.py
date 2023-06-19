Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1

    INF = 10 ** 10
    d = [[INF for _ in range(W)] for _ in range(H)]
    d[C_h][C_w] = 0

    q = [(C_h, C_w)]
    while q:
        h, w = q.pop(0)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h + dh, w + dw
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue
            if S[nh][nw] == '#':
                continue
            if d[nh][nw] != INF:
                continue
            d[nh][nw] = d[h][w]
            q.append((nh, nw))

        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W:
                    continue
                if S[nh][nw] == '#':
                    continue
                if d[nh][nw] != INF:
                    continue
                d[nh][nw] = d[h][w] + 1
                q.append((nh, nw))

    if d[D_h][D_w] == INF:
        print(-1)
    else:
        print(d[D_h][D_w])

solve()

=======
Suggestion 3

def main():
    # 读入数据
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    s = [input() for _ in range(h)]

    # 将坐标转化为索引
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1

    # 将坐标转化为索引
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1

    # 用来存储到达每个方格所需的魔法次数
    magic = [[float('inf')] * w for _ in range(h)]
    magic[c_h][c_w] = 0

    # 用来存储每个方格是否已经到达过
    visited = [[False] * w for _ in range(h)]

    # 用来存储待访问的方格
    queue = [(c_h, c_w)]

    # 朝上下左右四个方向移动
    for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nh = c_h + dh
        nw = c_w + dw
        if 0 <= nh < h and 0 <= nw < w and s[nh][nw] == '.':
            magic[nh][nw] = 0
            queue.append((nh, nw))

    # 广度优先搜索
    while queue:
        h, w = queue.pop(0)
        visited[h][w] = True
        # 朝上下左右四个方向移动
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < h and 0 <= nw < w and s[nh][nw] == '.' and not visited[nh][nw]:
                magic[nh][nw] = min(magic[nh][nw],

=======
Suggestion 4

def check(x,y):
    if x < 0 or x >= h:
        return False
    if y < 0 or y >= w:
        return False
    if s[x][y] == '#':
        return False
    return True

h,w = map(int,input().split())
ch,cw = map(int,input().split())
dh,dw = map(int,input().split())
s = [input() for _ in range(h)]
ch -= 1
cw -= 1
dh -= 1
dw -= 1
dist = [[-1]*w for _ in range(h)]
dist[ch][cw] = 0
q = [(ch,cw)]
while q:
    x,y = q.pop(0)
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx = x + dx
        ny = y + dy
        if not check(nx,ny):
            continue
        if dist[nx][ny] != -1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        q.append((nx,ny))
for i in range(h):
    for j in range(w):
        if dist[i][j] == -1:
            continue
        dist[i][j] = dist[i][j]//3

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    print(H,W,C_h,C_w,D_h,D_w)
    print(S)

=======
Suggestion 6

def problem176_d():
    H,W = map(int, input().split())
    C_h,C_w = map(int, input().split())
    D_h,D_w = map(int, input().split())
    S = [list(input()) for i in range(H)]
    C_h,C_w,D_h,D_w = C_h-1,C_w-1,D_h-1,D_w-1
    dist = [[-1]*W for i in range(H)]
    dist[C_h][C_w] = 0
    q = [(C_h,C_w)]
    while q:
        h,w = q.pop(0)
        for dh,dw in [(1,0),(0,1),(-1,0),(0,-1)]:
            nh,nw = h+dh,w+dw
            if nh<0 or nh>=H or nw<0 or nw>=W: continue
            if S[nh][nw] == '#': continue
            if dist[nh][nw] != -1: continue
            dist[nh][nw] = dist[h][w]
            q.append((nh,nw))
        for dh in range(-2,3):
            for dw in range(-2,3):
                nh,nw = h+dh,w+dw
                if nh<0 or nh>=H or nw<0 or nw>=W: continue
                if S[nh][nw] == '#': continue
                if dist[nh][nw] != -1: continue
                dist[nh][nw] = dist[h][w]+1
                q.append((nh,nw))
    print(dist[D_h][D_w])

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for i in range(H)]
    C_h, C_w, D_h, D_w = C_h - 1, C_w - 1, D_h - 1, D_w - 1
    D = [[-1] * W for i in range(H)]
    D[C_h][C_w] = 0
    Q = [(C_h, C_w)]
    while len(Q) > 0:
        i, j = Q.pop(0)
        for i2 in range(max(0, i - 2), min(H, i + 3)):
            for j2 in range(max(0, j - 2), min(W, j + 3)):
                if S[i2][j2] == '.' and D[i2][j2] == -1:
                    D[i2][j2] = D[i][j] + 1
                    Q.append((i2, j2))
    print(D[D_h][D_w])
