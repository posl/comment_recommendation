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
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    from collections import deque
    que = deque()
    que.append((C_h, C_w))
    dist = [[-1 for _ in range(W)] for _ in range(H)]
    dist[C_h][C_w] = 0
    while que:
        cur_h, cur_w = que.popleft()
        for dh, dw in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            next_h = cur_h + dh
            next_w = cur_w + dw
            if 0 <= next_h < H and 0 <= next_w < W and S[next_h][next_w] == '.' and dist[next_h][next_w] == -1:
                dist[next_h][next_w] = dist[cur_h][cur_w]
                que.appendleft((next_h, next_w))
        for i in range(-2, 3):
            for j in range(-2, 3):
                next_h = cur_h + i
                next_w = cur_w + j
                if 0 <= next_h < H and 0 <= next_w < W and S[next_h][next_w] == '.' and dist[next_h][next_w] == -1:
                    dist[next_h][next_w] = dist[cur_h][cur_w] + 1
                    que.append((next_h, next_w))
    print(dist[D_h][D_w])

=======
Suggestion 3

def main():
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    s = [input() for _ in range(h)]
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    inf = 10**9
    dist = [[inf for _ in range(w)] for _ in range(h)]
    dist[c_h][c_w] = 0
    que = []
    que.append((c_h, c_w))
    while len(que) > 0:
        now_h, now_w = que.pop(0)
        for i in range(-2, 3):
            for j in range(-2, 3):
                next_h = now_h + i
                next_w = now_w + j
                if next_h < 0 or next_h >= h or next_w < 0 or next_w >= w:
                    continue
                if s[next_h][next_w] == '#':
                    continue
                if dist[next_h][next_w] <= dist[now_h][now_w]:
                    continue
                dist[next_h][next_w] = dist[now_h][now_w]
                que.append((next_h, next_w))
        for i in range(-1, 2):
            for j in range(-1, 2):
                next_h = now_h + i
                next_w = now_w + j
                if next_h < 0 or next_h >= h or next_w < 0 or next_w >= w:
                    continue
                if dist[next_h][next_w] <= dist[now_h][now_w] + 1:
                    continue
                dist[next_h][next_w] = dist[now_h][now_w] + 1
                que.append((next_h, next_w))
    if dist[d_h][d_w] == inf:
        print(-1)
    else:
        print(dist[d_h][d_w])

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    queue = []
    queue.append((C_h, C_w))
    while queue:
        i, j = queue.pop(0)
        for i2, j2 in ((i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)):
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] != INF:
                continue
            dist[i2][j2] = dist[i][j]
            queue.append((i2, j2))
    for i in range(max(0, D_h - 2), min(H, D_h + 3)):
        for j in range(max(0, D_w - 2), min(W, D_w + 3)):
            if S[i][j] == '#':
                continue
            dist[i][j] += 1
    if dist[D_h][D_w] == INF:
        print(-1)
    else:
        print(dist[D_h][D_w])

=======
Suggestion 5

def dfs(i, j, k):
    if i == dh and j == dw:
        return k
    if k >= 3:
        return -1
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    res = 10**9
    for di, dj in d:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '.':
            res = min(res, dfs(ni, nj, k))
        else:
            for di2, dj2 in d:
                ni2, nj2 = ni + di2, nj + dj2
                if 0 <= ni2 < h and 0 <= nj2 < w and s[ni2][nj2] == '.':
                    res = min(res, dfs(ni2, nj2, k + 1))
    dp[i][j][k] = res
    return res

h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch, cw, dh, dw = ch - 1, cw - 1, dh - 1, dw - 1
s = [input() for _ in range(h)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
dp = [[[-1] * 4 for _ in range(w)] for _ in range(h)]
print(dfs(ch, cw, 0))

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    Ch,Cw = map(int,input().split())
    Dh,Dw = map(int,input().split())
    S = [input() for _ in range(H)]
    Ch -= 1
    Cw -= 1
    Dh -= 1
    Dw -= 1
    #print(H,W,Ch,Cw,Dh,Dw)
    #print(S)
    #print(S[0][0])
    #print(S[0][1])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[2][3])
    #print(S[3][2])
    #print(S[3][3])
    #print(S[3][4])
    #print(S[4][3])
    #print(S[4][4])
    #print(S[4][5])
    #print(S[5][4])
    #print(S[5][5])
    #print(S[5][6])
    #print(S[6][5])
    #print(S[6][6])
    #print(S[6][7])
    #print(S[7][6])
    #print(S[7][7])
    #print(S[7][8])
    #print(S[8][7])
    #print(S[8][8])
    #print(S[8][9])
    #print(S[9][8])
    #print(S[9][9])
    #print(S[9][10])
    #print(S[10][9])
    #print(S[10][10])
    #print(S[10][11])
    #print(S[11][10])
    #print(S[11][11])
    #print(S[11][12])
    #print(S[12][11])
    #print(S[12][12])
    #print(S[12][13])
    #print(S[13][12])
    #print(S[13][13])
    #print(S[13][14])
    #print(S[14][13])
    #print(S[14][14])
    #print(S[14][15])
    #print(S[15][14])
    #print(S[

=======
Suggestion 7

def main():
    print("Hello World!")
