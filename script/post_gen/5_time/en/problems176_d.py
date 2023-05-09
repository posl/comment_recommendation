Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for i in range(H)]

    def bfs(S, C_h, C_w, D_h, D_w):
        from collections import deque
        q = deque()
        q.append((C_h-1, C_w-1))
        dist = [[float('inf')] * W for i in range(H)]
        dist[C_h-1][C_w-1] = 0
        while q:
            i, j = q.popleft()
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                if S[ni][nj] == '#':
                    continue
                if dist[ni][nj] > dist[i][j]:
                    dist[ni][nj] = dist[i][j]
                    q.appendleft((ni, nj))
            for di in range(-2, 3):
                for dj in range(-2, 3):
                    ni, nj = i + di, j + dj
                    if not (0 <= ni < H and 0 <= nj < W):
                        continue
                    if S[ni][nj] == '#':
                        continue
                    if dist[ni][nj] > dist[i][j] + 1:
                        dist[ni][nj] = dist[i][j] + 1
                        q.append((ni, nj))
        return dist[D_h-1][D_w-1]

    ans = bfs(S, C_h, C_w, D_h, D_w)
    print(ans)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    #print(H, W, C_h, C_w, D_h, D_w)
    #print(S)
    S[C_h-1][C_w-1] = 0
    S[D_h-1][D_w-1] = 0
    #print(S)
    #print()
    #print(S)
    #print()
    #print(S[0][0])
    #print(S[0][1])
    #print(S[0][2])
    #print(S[0][3])
    #print(S[0][4])
    #print(S[1][0])
    #print(S[1][1])
    #print(S[1][2])
    #print(S[1][3])
    #print(S[1][4])
    #print(S[2][0])
    #print(S[2][1])
    #print(S[2][2])
    #print(S[2][3])
    #print(S[2][4])
    #print(S[3][0])
    #print(S[3][1])
    #print(S[3][2])
    #print(S[3][3])
    #print(S[3][4])
    #print()
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print()
    #print(S[0][0])
    #print(S[1][0])
    #print(S[2][0])
    #print(S[3][0])
    #print(S[4][0])
    #print(S[0][1])
    #print(S[1][1])
    #print(S[2][1])
    #print(S[3][1])
    #print(S[4][1])
    #print(S[0][2])
    #print(S[1][2])
    #print(S[2][2])
    #print(S[3][2])
    #print(S[4][2])
    #print(S[0][3])
    #print(S[1][3])
    #

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for i in range(H)]

    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1

    from collections import deque
    q = deque()
    q.append((C_h, C_w))
    dist = [[-1] * W for i in range(H)]
    dist[C_h][C_w] = 0

    while q:
        h, w = q.popleft()
        for dh, dw in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nh = h + dh
            nw = w + dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if S[nh][nw] == "#":
                continue
            if dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w]
                q.appendleft((nh, nw))

    ans = dist[D_h][D_w]
    print(ans)

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[float("inf") for _ in range(W)] for _ in range(H)]
    dist[C_h][C_w] = 0
    que = [(C_h, C_w, 0)]
    while que:
        h, w, d = que.pop(0)
        if h == D_h and w == D_w:
            break
        for i, j in ((h-1, w), (h+1, w), (h, w-1), (h, w+1)):
            if 0 <= i < H and 0 <= j < W and S[i][j] == "." and dist[i][j] > d:
                dist[i][j] = d
                que.append((i, j, d))
        for i in range(h-2, h+3):
            for j in range(w-2, w+3):
                if 0 <= i < H and 0 <= j < W and S[i][j] == "." and dist[i][j] > d+1:
                    dist[i][j] = d+1
                    que.append((i, j, d+1))
    if dist[D_h][D_w] == float("inf"):
        print(-1)
    else:
        print(dist[D_h][D_w])

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[float("inf")] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    que = [(C_h, C_w)]
    while que:
        h, w = que.pop(0)
        if h == D_h and w == D_w:
            break
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h + dh, w + dw
            if nh < 0 or nh >= H or nw < 0 or nw >= W or S[nh][nw] == "#" or dist[nh][nw] <= dist[h][w]:
                continue
            dist[nh][nw] = dist[h][w]
            que.insert(0, (nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W or S[nh][nw] == "#" or dist[nh][nw] <= dist[h][w] + 1:
                    continue
                dist[nh][nw] = dist[h][w] + 1
                que.append((nh, nw))
    print(dist[D_h][D_w] if dist[D_h][D_w] < float("inf") else -1)

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for i in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    dist = [[-1 for j in range(W)] for i in range(H)]
    dist[C_h][C_w] = 0
    q = [(C_h, C_w)]
    while len(q) > 0:
        i, j = q.pop(0)
        for i2 in range(i - 2, i + 3):
            for j2 in range(j - 2, j + 3):
                if 0 <= i2 < H and 0 <= j2 < W and S[i2][j2] == "." and dist[i2][j2] == -1:
                    dist[i2][j2] = dist[i][j] + 1
                    q.append((i2, j2))
    print(dist[D_h][D_w])

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    maze = [list(input()) for _ in range(h)]
    maze = [['#'] + m + ['#'] for m in maze]
    maze = [['#' for _ in range(w+2)]] + maze + [['#' for _ in range(w+2)]]
    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
    visited[ch][cw] = True
    queue = [(ch, cw, 0)]
    while queue:
        x, y, d = queue.pop(0)
        if x == dh and y == dw:
            print(d)
            return
        for i, j in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
            if maze[i][j] == '.' and not visited[i][j]:
                visited[i][j] = True
                queue.append((i, j, d))
        for i in range(x-2, x+3):
            for j in range(y-2, y+3):
                if maze[i][j] == '.' and not visited[i][j]:
                    visited[i][j] = True
                    queue.append((i, j, d+1))
    print(-1)

main()

=======
Suggestion 8

def main():
    import sys
    sys.setrecursionlimit(1000000)
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    visited = [[0] * W for _ in range(H)]
    def dfs(i, j, cnt):
        if i < 0 or i >= H or j < 0 or j >= W or S[i][j] == '#' or visited[i][j]:
            return 10**9
        if i == D_h and j == D_w:
            return cnt
        visited[i][j] = 1
        res = 10**9
        res = min(res, dfs(i - 1, j, cnt + 1))
        res = min(res, dfs(i + 1, j, cnt + 1))
        res = min(res, dfs(i, j - 1, cnt + 1))
        res = min(res, dfs(i, j + 1, cnt + 1))
        res = min(res, dfs(i - 2, j - 2, cnt + 1))
        res = min(res, dfs(i - 2, j - 1, cnt + 1))
        res = min(res, dfs(i - 2, j, cnt + 1))
        res = min(res, dfs(i - 2, j + 1, cnt + 1))
        res = min(res, dfs(i - 2, j + 2, cnt + 1))
        res = min(res, dfs(i - 1, j - 2, cnt + 1))
        res = min(res, dfs(i - 1, j + 2, cnt + 1))
        res = min(res, dfs(i, j - 2, cnt + 1))
        res = min(res, dfs(i, j + 2, cnt + 1))
        res = min(res, dfs(i + 1, j - 2, cnt + 1))
        res = min(res, dfs(i + 1, j + 2, cnt +

=======
Suggestion 9

def main():
    h,w = map(int,input().split())
    c_h,c_w = map(int,input().split())
    d_h,d_w = map(int,input().split())
    s = [input() for i in range(h)]
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    q = [(c_h,c_w,0)]
    visited = {(c_h,c_w)}
    while q:
        c_h,c_w,c = q.pop(0)
        if c_h == d_h and c_w == d_w:
            print(c)
            return
        for i,j in [(c_h+1,c_w),(c_h-1,c_w),(c_h,c_w+1),(c_h,c_w-1)]:
            if 0<=i<h and 0<=j<w and s[i][j] == '.' and (i,j) not in visited:
                q.append((i,j,c))
                visited.add((i,j))
        for i in range(-2,3):
            for j in range(-2,3):
                if 0<=c_h+i<h and 0<=c_w+j<w and s[c_h+i][c_w+j] == '.' and (c_h+i,c_w+j) not in visited:
                    q.append((c_h+i,c_w+j,c+1))
                    visited.add((c_h+i,c_w+j))
    print(-1)

=======
Suggestion 10

def main():
    pass
