Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1

    # print(H, W)
    # print(C_h, C_w)
    # print(D_h, D_w)
    # print(S)

    # 0: 壁
    # 1: 道
    # 2: 魔法使いの位置
    # 3: 目的地の位置
    # 4: 未訪問
    # 5: 訪問済み
    S_ = [[0 if S[i][j] == "#" else 1 for j in range(W)] for i in range(H)]
    S_[C_h][C_w] = 2
    S_[D_h][D_w] = 3
    # print(S_)

    # 0: 壁
    # 1: 道
    # 2: 魔法使いの位置
    # 3: 目的地の位置
    # 4: 未訪問
    # 5: 訪問済み
    # 6: ワープ魔法で訪問済み
    S_warp = [[0 if S[i][j] == "#" else 1 for j in range(W)] for i in range(H)]
    S_warp[C_h][C_w] = 2
    S_warp[D_h][D_w] = 3
    # print(S_warp)

    # 移動A
    # 移動B
    # 4: 未訪問
    # 5: 訪問済み
    # 6: ワープ魔法で訪問済み
    # 7: ワープ魔法で訪問済み(5x5範囲内)
    # 8: ワープ魔法で訪

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
    # print(H, W)
    # print(C_h, C_w)
    # print(D_h, D_w)
    # print(S)
    # print(S[C_h][C_w])
    # print(S[D_h][D_w])
    import queue
    q = queue.Queue()
    q.put((C_h, C_w))
    dist = [[-1] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    while not q.empty():
        h, w = q.get()
        # print(h, w)
        # print(dist)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w] + 1
                q.put((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    q.put((nh, nw))
    print(dist[D_h][D_w])

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]

    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1

    INF = 10 ** 10
    # 魔法使用回数
    magic = [[INF] * W for _ in range(H)]
    magic[C_h][C_w] = 0

    # 移動可能かどうか
    can_move = [[False] * W for _ in range(H)]
    can_move[C_h][C_w] = True

    # 移動可能なマスを探索するキュー
    que = [(C_h, C_w)]

    while que:
        h, w = que.pop(0)

        # 移動可能なマスを探索
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh = h + dh
            nw = w + dw

            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == ".":
                if not can_move[nh][nw]:
                    can_move[nh][nw] = True
                    que.append((nh, nw))

    # 周囲5マスを探索
    for h in range(H):
        for w in range(W):
            if not can_move[h][w]:
                continue

            for dh in range(-2, 3):
                for dw in range(-2, 3):
                    nh = h + dh
                    nw = w + dw

                    if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == ".":
                        can_move[nh][nw] = True

    # 移動可能なマスを探索するキュー
    que = [(C_h, C_w)]

    while que:
        h, w = que.pop(0)

        # 移動可能なマスを探索
        for dh, dw in ((1, 0),

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    Ch, Cw = map(int, input().split())
    Dh, Dw = map(int, input().split())
    S = [input() for _ in range(H)]
    C = [[-1]*W for _ in range(H)]
    C[Ch-1][Cw-1] = 0
    Q = [(Ch-1, Cw-1)]
    while Q:
        h, w = Q.pop()
        if h < H-1 and S[h+1][w] == "." and C[h+1][w] == -1:
            C[h+1][w] = C[h][w]
            Q.append((h+1, w))
        if h > 0 and S[h-1][w] == "." and C[h-1][w] == -1:
            C[h-1][w] = C[h][w]
            Q.append((h-1, w))
        if w < W-1 and S[h][w+1] == "." and C[h][w+1] == -1:
            C[h][w+1] = C[h][w]
            Q.append((h, w+1))
        if w > 0 and S[h][w-1] == "." and C[h][w-1] == -1:
            C[h][w-1] = C[h][w]
            Q.append((h, w-1))
        for i in range(-2, 3):
            for j in range(-2, 3):
                if h+i < 0 or h+i >= H or w+j < 0 or w+j >= W or S[h+i][w+j] == "#":
                    continue
                if C[h+i][w+j] == -1:
                    C[h+i][w+j] = C[h][w]+1
                    Q.append((h+i, w+j))
    print(C[Dh-1][Dw-1])

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    S = [input() for _ in range(H)]
    INF = 10**10
    d = [[INF] * W for _ in range(H)]
    d[ch-1][cw-1] = 0
    q = [(ch-1, cw-1)]
    while q:
        h, w = q.pop(0)
        for nh, nw in [(h-1, w), (h+1, w), (h, w-1), (h, w+1)]:
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and d[nh][nw] == INF:
                d[nh][nw] = d[h][w] + 1
                q.append((nh, nw))
        for nh in range(h-2, h+3):
            for nw in range(w-2, w+3):
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and d[nh][nw] == INF:
                    d[nh][nw] = d[h][w] + 1
                    q.append((nh, nw))
    print(d[dh-1][dw-1] if d[dh-1][dw-1] != INF else -1)

=======
Suggestion 6

def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = []
    for i in range(H):
        S.append(input())
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    ans = solve(H,W,C_h,C_w,D_h,D_w,S)
    print(ans)

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    CH, CW = map(int, input().split())
    DH, DW = map(int, input().split())
    S = [input() for _ in range(H)]
    CH -= 1
    CW -= 1
    DH -= 1
    DW -= 1

    # 移動A
    def moveA(x, y):
        return [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]

    # 移動B
    def moveB(x, y):
        return [(x+i, y+j) for i in range(-2, 3) for j in range(-2, 3)]

    # 移動
    def move(x, y):
        return moveA(x, y) + moveB(x, y)

    # ワープ魔法を使う回数
    warp = [[-1]*W for _ in range(H)]
    warp[CH][CW] = 0

    # 移動回数
    move_count = [[-1]*W for _ in range(H)]
    move_count[CH][CW] = 0

    # 幅優先探索
    queue = [(CH, CW)]
    while queue:
        x, y = queue.pop(0)
        for next_x, next_y in move(x, y):
            if not 0 <= next_x < H or not 0 <= next_y < W:
                continue
            if S[next_x][next_y] == '#':
                continue
            if warp[next_x][next_y] == -1:
                warp[next_x][next_y] = warp[x][y] + 1
                move_count[next_x][next_y] = move_count[x][y] + 1
                queue.append((next_x, next_y))
            elif warp[next_x][next_y] == warp[x][y]:
                if move_count[next_x][next_y] > move_count[x][y] + 1:
                    move_count[next_x][next_y] = move_count[x][y] + 1
                    queue.append((next_x, next_y))

    print(warp[DH][DW])

=======
Suggestion 8

def main():
    from collections import deque
    import sys
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    dh = [0, 1, 0, -1]
    dw = [1, 0, -1, 0]
    q = deque()
    q.append((C_h-1, C_w-1, 0))
    while q:
        h, w, cnt = q.popleft()
        if h == D_h-1 and w == D_w-1:
            print(cnt)
            sys.exit()
        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                S[nh][nw] = '#'
                q.append((nh, nw, cnt))
        for i in range(-2, 3):
            for j in range(-2, 3):
                nh = h + i
                nw = w + j
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.':
                    S[nh][nw] = '#'
                    q.append((nh, nw, cnt+1))
    print(-1)

=======
Suggestion 9

def main():
    #入力
    H,W = map(int,input().split())
    Ch,Cw = map(int,input().split())
    Dh,Dw = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    #print(H,W,Ch,Cw,Dh,Dw,S)

    #初期化
    INF = 10**9
    dist = [[INF]*W for _ in range(H)]

    #bfs
    import collections
    q = collections.deque()
    q.append((Ch-1,Cw-1))
    dist[Ch-1][Cw-1] = 0
    while q:
        h,w = q.popleft()
        #print(h,w)
        #移動A
        for dh,dw in [(0,1),(0,-1),(1,0),(-1,0)]:
            if 0<=h+dh<H and 0<=w+dw<W and S[h+dh][w+dw]=="." and dist[h][w]+1<dist[h+dh][w+dw]:
                dist[h+dh][w+dw] = dist[h][w]+1
                q.append((h+dh,w+dw))
        #移動B
        for dh in range(-2,3):
            for dw in range(-2,3):
                if 0<=h+dh<H and 0<=w+dw<W and S[h+dh][w+dw]=="." and dist[h][w]+1<dist[h+dh][w+dw]:
                    dist[h+dh][w+dw] = dist[h][w]+1
                    q.append((h+dh,w+dw))

    if dist[Dh-1][Dw-1]==INF:
        print(-1)
    else:
        print(dist[Dh-1][Dw-1])

=======
Suggestion 10

def main():
    #入力
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    C_h -= 1
    C_w -= 1
    D_h,D_w = map(int,input().split())
    D_h -= 1
    D_w -= 1
    S = []
    for i in range(H):
        S.append(list(input()))
    #print(H,W,C_h,C_w,D_h,D_w,S)

    #移動可能かどうか
    if S[D_h][D_w] == "#":
        print(-1)
        return

    #移動可能なマスを保存
    S[C_h][C_w] = 0
    S[D_h][D_w] = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == ".":
                S[i][j] = -1

    #移動可能なマスを保存
    #print(S)
    for i in range(H):
        for j in range(W):
            if S[i][j] == 0:
                #print(i,j)
                for k in range(-2,3):
                    for l in range(-2,3):
                        if 0 <= i+k < H and 0 <= j+l < W and S[i+k][j+l] != "#":
                            if abs(k) + abs(l) == 1:
                                S[i+k][j+l] = 0
                            else:
                                S[i+k][j+l] = 1
    #print(S)
    #print(S[D_h][D_w])
    if S[D_h][D_w] == -1:
        print(-1)
        return

    #移動可能なマスを保存
    #print(S)
    for i in range(H):
        for j in range(W):
            if S[i][j] == 0:
                #print(i,j)
                for k in range(-2,3):
                    for l in range(-2,3):
                        if 0 <= i+k < H and 0 <= j+l < W and S[i+k][j+l] != "#":
                            if abs(k) + abs(l) == 1:
                                S[i+k][j+l] = 0
                            else:
                                S[i+k][j
