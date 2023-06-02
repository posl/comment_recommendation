Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def get_input():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    return H, W, C_h, C_w, D_h, D_w, S

=======
Suggestion 3

def main():
    h,w = map(int,input().split())
    c_h,c_w = map(int,input().split())
    d_h,d_w = map(int,input().split())
    s = [input() for i in range(h)]
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    #print(h,w,c_h,c_w,d_h,d_w,s)
    visited = [[False]*w for i in range(h)]
    visited[c_h][c_w] = True
    q = []
    q.append((c_h,c_w,0))
    while len(q) > 0:
        (ch,cw,step) = q.pop(0)
        #print(ch,cw,step)
        if ch == d_h and cw == d_w:
            print(step)
            return
        for (dh,dw) in [(0,1),(0,-1),(1,0),(-1,0)]:
            nh = ch + dh
            nw = cw + dw
            if nh >= 0 and nh < h and nw >= 0 and nw < w and s[nh][nw] == '.' and visited[nh][nw] == False:
                visited[nh][nw] = True
                q.append((nh,nw,step))
        for dh in range(-2,3):
            for dw in range(-2,3):
                nh = ch + dh
                nw = cw + dw
                if nh >= 0 and nh < h and nw >= 0 and nw < w and s[nh][nw] == '.' and visited[nh][nw] == False:
                    visited[nh][nw] = True
                    q.append((nh,nw,step+1))
    print(-1)

=======
Suggestion 4

def main():
    # 读入数据
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    # 求解
    # 从(C_h, C_w)到(D_h, D_w)的最短距离
    dist = [[-1] * W for _ in range(H)]
    dist[C_h - 1][C_w - 1] = 0
    queue = [(C_h - 1, C_w - 1)]
    while queue:
        i, j = queue.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] != -1:
                continue
            dist[i2][j2] = dist[i][j] + 1
            queue.append((i2, j2))
    # 从(D_h, D_w)到(C_h, C_w)的最短距离
    dist2 = [[-1] * W for _ in range(H)]
    dist2[D_h - 1][D_w - 1] = 0
    queue = [(D_h - 1, D_w - 1)]
    while queue:
        i, j = queue.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist2[i2][j2] != -1:
                continue
            dist2[i2][j2] = dist2[i][j] + 1
            queue.append((i2, j2))

    # 从

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    visited = [[float("inf") for _ in range(W)] for _ in range(H)]
    visited[C_h][C_w] = 0
    queue = [(C_h,C_w)]
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    while queue:
        h,w = queue.pop(0)
        if h == D_h and w == D_w:
            break
        for dh,dw in d:
            if 0 <= h+dh < H and 0 <= w+dw < W and S[h+dh][w+dw] == "." and visited[h+dh][w+dw] == float("inf"):
                visited[h+dh][w+dw] = visited[h][w]
                queue.append((h+dh,w+dw))
        for dh in range(-2,3):
            for dw in range(-2,3):
                if 0 <= h+dh < H and 0 <= w+dw < W and S[h+dh][w+dw] == "." and visited[h+dh][w+dw] == float("inf"):
                    visited[h+dh][w+dw] = visited[h][w] + 1
                    queue.append((h+dh,w+dw))
    if visited[D_h][D_w] == float("inf"):
        print(-1)
    else:
        print(visited[D_h][D_w])
