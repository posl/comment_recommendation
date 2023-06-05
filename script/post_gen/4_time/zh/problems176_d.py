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
    S = [input() for _ in range(H)]
    C_h, C_w, D_h, D_w = C_h-1, C_w-1, D_h-1, D_w-1
    dist = [[-1]*W for _ in range(H)]
    dist[C_h][C_w] = 0
    queue = [(C_h, C_w)]
    while queue:
        h, w = queue.pop(0)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h+dh, w+dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                queue.append((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h+dh, w+dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    queue.append((nh, nw))
    print(dist[D_h][D_w])

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    C_h, C_w, D_h, D_w = C_h - 1, C_w - 1, D_h - 1, D_w - 1

    from collections import deque
    q = deque([(C_h, C_w)])
    dist = [[-1] * W for _ in range(H)]
    dist[C_h][C_w] = 0

    while q:
        i, j = q.popleft()
        for i2, j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] != -1:
                continue
            dist[i2][j2] = dist[i][j]
            q.appendleft((i2, j2))
        for i2 in range(i - 2, i + 3):
            for j2 in range(j - 2, j + 3):
                if not (0 <= i2 < H and 0 <= j2 < W):
                    continue
                if S[i2][j2] == '#':
                    continue
                if dist[i2][j2] != -1:
                    continue
                dist[i2][j2] = dist[i][j] + 1
                q.append((i2, j2))

    print(dist[D_h][D_w])

=======
Suggestion 4

def get_input():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    return H,W,C_h,C_w,D_h,D_w,S

=======
Suggestion 5

def solve():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1
    s = [input() for _ in range(h)]
    d = [[-1] * w for _ in range(h)]
    d[ch][cw] = 0
    q = []
    q.append((ch, cw))
    while q:
        i, j = q.pop(0)
        for i2 in range(i - 2, i + 3):
            for j2 in range(j - 2, j + 3):
                if not (0 <= i2 < h and 0 <= j2 < w):
                    continue
                if s[i2][j2] == '#':
                    continue
                if d[i2][j2] != -1:
                    continue
                if abs(i2 - i) + abs(j2 - j) == 1:
                    d[i2][j2] = d[i][j]
                    q.append((i2, j2))
                else:
                    d[i2][j2] = d[i][j] + 1
                    q.append((i2, j2))
    print(d[dh][dw])


solve()

=======
Suggestion 6

def main():
    return

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = [list(input()) for i in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    Q = deque()
    Q.append((C_h,C_w,0))
    dist = [[-1]*W for i in range(H)]
    dist[C_h][C_w] = 0
    while Q:
        i,j,d = Q.popleft()
        for i2,j2 in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] == -1:
                dist[i2][j2] = d
                Q.appendleft((i2,j2,d))
        for i2 in range(i-2,i+3):
            for j2 in range(j-2,j+3):
                if not (0 <= i2 < H and 0 <= j2 < W):
                    continue
                if S[i2][j2] == '#':
                    continue
                if dist[i2][j2] == -1:
                    dist[i2][j2] = d + 1
                    Q.append((i2,j2,d+1))
    print(dist[D_h][D_w])
