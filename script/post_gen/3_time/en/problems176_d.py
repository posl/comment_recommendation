Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h, C_w, D_h, D_w = C_h-1, C_w-1, D_h-1, D_w-1
    from collections import deque
    q = deque([(C_h, C_w, 0)])
    d = [[-1]*W for _ in range(H)]
    d[C_h][C_w] = 0
    while q:
        i, j, k = q.popleft()
        if i == D_h and j == D_w:
            print(k)
            return
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '.' and d[ni][nj] == -1:
                d[ni][nj] = k
                q.appendleft((ni, nj, k))
        for di in range(-2, 3):
            for dj in range(-2, 3):
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '.' and d[ni][nj] == -1:
                    d[ni][nj] = k + 1
                    q.append((ni, nj, k + 1))
    print(-1)

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for i in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    INF = 10 ** 9
    dist = [[INF for i in range(W)] for j in range(H)]
    dist[C_h][C_w] = 0
    q = []
    q.append([C_h, C_w])
    while len(q) > 0:
        h, w = q.pop(0)
        if h == D_h and w == D_w:
            break
        if h > 0 and S[h - 1][w] == '.' and dist[h - 1][w] > dist[h][w]:
            dist[h - 1][w] = dist[h][w]
            q.append([h - 1, w])
        if h < H - 1 and S[h + 1][w] == '.' and dist[h + 1][w] > dist[h][w]:
            dist[h + 1][w] = dist[h][w]
            q.append([h + 1, w])
        if w > 0 and S[h][w - 1] == '.' and dist[h][w - 1] > dist[h][w]:
            dist[h][w - 1] = dist[h][w]
            q.append([h, w - 1])
        if w < W - 1 and S[h][w + 1] == '.' and dist[h][w + 1] > dist[h][w]:
            dist[h][w + 1] = dist[h][w]
            q.append([h, w + 1])
        for i in range(-2, 3):
            for j in range(-2, 3):
                if h + i < 0 or h + i >= H or w + j < 0 or w + j >= W:
                    continue
                if S[h + i][w + j] == '#' or dist[h + i][w + j] <= dist[h][w] + 1:
                    continue
                dist[h + i][

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    INF = 10**10
    dist = [[INF] * W for _ in range(H)]
    dist[Ch-1][Cw-1] = 0

    def bfs():
        from collections import deque
        q = deque()
        q.append((Ch-1, Cw-1))
        while q:
            h, w = q.popleft()
            if h == Dh-1 and w == Dw-1:
                return dist[h][w]
            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == INF:
                    dist[nh][nw] = dist[h][w]
                    q.appendleft((nh, nw))
            for dh in range(-2, 3):
                for dw in range(-2, 3):
                    nh, nw = h + dh, w + dw
                    if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == INF:
                        dist[nh][nw] = dist[h][w] + 1
                        q.append((nh, nw))
        return -1

    print(bfs())

main()

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    dist[ch][cw] = 0
    from collections import deque
    q = deque()
    q.append((ch, cw))
    while q:
        h, w = q.popleft()
        for dh, dw in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == INF:
                dist[nh][nw] = dist[h][w]
                q.appendleft((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == INF:
                    dist[nh][nw] = dist[h][w] + 1
                    q.append((nh, nw))
    if dist[dh][dw] == INF:
        print(-1)
    else:
        print(dist[dh][dw])

main()

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ch -= 1
    cw -= 1
    dh -= 1
    dw -= 1
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    dist[ch][cw] = 0
    queue = [(ch, cw)]
    while queue:
        h, w = queue.pop(0)
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] > dist[h][w]:
                dist[nh][nw] = dist[h][w]
                queue.append((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] > dist[h][w] + 1:
                    dist[nh][nw] = dist[h][w] + 1
                    queue.append((nh, nw))
    if dist[dh][dw] == INF:
        print(-1)
    else:
        print(dist[dh][dw])

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    C_h -= 1
    C_w -= 1
    D_h, D_w = map(int, input().split())
    D_h -= 1
    D_w -= 1
    S = []
    for h in range(H):
        S.append(list(input()))
    Q = []
    Q.append([C_h, C_w, 0])
    S[C_h][C_w] = 1
    while len(Q) > 0:
        h, w, c = Q.pop(0)
        if h == D_h and w == D_w:
            print(c)
            return
        for dh, dw in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= h + dh < H and 0 <= w + dw < W and S[h + dh][w + dw] == ".":
                S[h + dh][w + dw] = c + 1
                Q.append([h + dh, w + dw, c + 1])
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                if 0 <= h + dh < H and 0 <= w + dw < W and S[h + dh][w + dw] == ".":
                    S[h + dh][w + dw] = c + 1
                    Q.append([h + dh, w + dw, c + 1])
    print(-1)
    return

main()

I wrote a solution in python3. It is easy to understand, but it is not efficient. It is O(HW) in time complexity.

I think this problem is a kind of BFS.

I think this problem is a kind of BFS.

Yes, it is.

Thanks for your answer. I think I should try to use BFS in the future.

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(input())

    #print(H,W)
    #print(C_h,C_w)
    #print(D_h,D_w)
    #print(S)

    #A: 1マス移動
    #B: 5*5の範囲内で移動
    #A or Bを繰り返す

    #Aの場合は、上下左右に移動可能
    #

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    CH, CW = map(int, input().split())
    DH, DW = map(int, input().split())
    S = [[c for c in input()] for _ in range(H)]
    print(solve(H, W, CH - 1, CW - 1, DH - 1, DW - 1, S))

=======
Suggestion 9

def main():
    H,W=map(int,input().split())
    CH,CW=map(int,input().split())
    DH,DW=map(int,input().split())
    S=[input() for i in range(H)]
    INF=10**9
    dp=[[INF]*W for i in range(H)]
    dp[CH-1][CW-1]=0
    for i in range(H):
        for j in range(W):
            if S[i][j]=="#":
                continue
            for k in range(-2,3):
                for l in range(-2,3):
                    if 0<=i+k<H and 0<=j+l<W and S[i+k][j+l]=="." and dp[i+k][j+l]>dp[i][j]+(abs(k)+abs(l)>1):
                        dp[i+k][j+l]=dp[i][j]+(abs(k)+abs(l)>1)
    if dp[DH-1][DW-1]==INF:
        print(-1)
    else:
        print(dp[DH-1][DW-1])

=======
Suggestion 10

def get_input(): #input
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    return H,W,C_h,C_w,D_h,D_w,S
