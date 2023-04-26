Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    
    # 0: 未探索, 1: 探索済み, 2: 探索中
    state = [[0] * W for _ in range(H)]
    dist = [[-1] * W for _ in range(H)]
    
    def dfs(h, w, d):
        if state[h][w] == 2:
            return
        if state[h][w] == 1:
            if dist[h][w] <= d:
                return
            else:
                print(-1)
                exit()
        dist[h][w] = d
        state[h][w] = 2
        for dh, dw in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nh, nw = h + dh, w + dw
            if 0 <= nh < H and 0 <= nw < W:
                if S[nh][nw] == '.':
                    dfs(nh, nw, d + 1)
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if 0 <= nh < H and 0 <= nw < W:
                    if S[nh][nw] == '.':
                        dfs(nh, nw, d + 1)
        state[h][w] = 1
    
    dfs(C_h - 1, C_w - 1, 0)
    print(dist[D_h - 1][D_w - 1])

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

    # ワープ魔法の範囲
    warp_range = 2
    # ワープ魔法の範囲を考慮した迷路
    warp_S = [['#' for _ in range(W + warp_range * 2)] for _ in range(H + warp_range * 2)]
    # ワープ魔法の範囲を考慮した現在地
    warp_C_h = C_h + warp_range
    warp_C_w = C_w + warp_range
    # ワープ魔法の範囲を考慮したゴール
    warp_D_h = D_h + warp_range
    warp_D_w = D_w + warp_range
    # ワープ魔法の範囲を考慮した迷路を作成
    for i in range(H):
        for j in range(W):
            warp_S[i + warp_range][j + warp_range] = S[i][j]

    # 移動可能な座標を格納するリスト
    movable = []
    # 移動可能な座標を追加
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                movable.append((i, j))
    # 移動可能な座標の数
    movable_num = len(movable)
    # 移動可能な座標に対応するワープ魔法の使用回数を格納するリスト
    warp_num = [-1 for _ in range(movable_num)]

    # ワープ魔法の使用回数を計算
    for i in range(movable_num):
        warp_num[i] = abs(movable

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    
    # (C_h, C_w) から (D_h, D_w) への最短距離を求める
    # 距離の初期化
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    dist[C_h-1][C_w-1] = 0
    
    # 1回目のBFS
    # 移動Aのみで到達可能なマスを全てキューに入れる
    from collections import deque
    q = deque()
    q.append((C_h-1, C_w-1))
    while q:
        h, w = q.popleft()
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dh += h
            dw += w
            if 0 <= dh < H and 0 <= dw < W and S[dh][dw] == '.' and dist[dh][dw] == INF:
                dist[dh][dw] = dist[h][w] + 1
                q.append((dh, dw))
    
    # 2回目のBFS
    # 移動Aのみで到達可能なマスから、移動Bで到達可能なマスを全てキューに入れる
    q = deque()
    for h in range(H):
        for w in range(W):
            if dist[h][w] <= 2:
                q.append((h, w))
                dist[h][w] = 0
    while q:
        h, w = q.popleft()
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                dh += h
                dw += w
                if 0 <= dh < H and 0 <= dw < W and S[dh][dw] == '.' and dist[dh][dw] == INF:
                    dist[dh][dw

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1

    # スタート地点からの最短距離
    dist = [[-1] * W for _ in range(H)]
    dist[C_h][C_w] = 0

    # スタート地点からの最短距離をBFSで求める
    from collections import deque
    q = deque()
    q.append((C_h, C_w))
    while q:
        h, w = q.popleft()
        # 移動A
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                dist[nh][nw] = dist[h][w] + 1
                q.append((nh, nw))
        # 移動B
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] == -1:
                    dist[nh][nw] = dist[h][w] + 1
                    q.append((nh, nw))

    print(dist[D_h][D_w])

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = []
    for i in range(H):
        S.append(list(input()))

    #スタート地点とゴール地点の座標を0始まりにする
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1

    #スタート地点からの距離を記録する
    dist = [[float('inf') for i in range(W)] for j in range(H)]
    dist[C_h][C_w] = 0

    #スタート地点からの距離を更新する
    queue = [[C_h, C_w]]
    while queue:
        h, w = queue.pop(0)
        #移動A
        for dh, dw in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nh = h + dh
            nw = w + dw
            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] > dist[h][w]:
                dist[nh][nw] = dist[h][w]
                queue.append([nh, nw])
        #移動B
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh = h + dh
                nw = w + dw
                if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == '.' and dist[nh][nw] > dist[h][w] + 1:
                    dist[nh][nw] = dist[h][w] + 1
                    queue.append([nh, nw])

    if dist[D_h][D_w] == float('inf'):
        print(-1)
    else:
        print(dist[D_h][D_w])

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    dist = [[-1]*w for _ in range(h)]
    dist[ch-1][cw-1] = 0
    q = [(ch-1, cw-1)]
    while q:
        nh, nw = q.pop(0)
        for dh, dw in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nh2, nw2 = nh+dh, nw+dw
            if 0 <= nh2 < h and 0 <= nw2 < w and s[nh2][nw2] == "." and dist[nh2][nw2] == -1:
                dist[nh2][nw2] = dist[nh][nw]
                q.append((nh2, nw2))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh2, nw2 = nh+dh, nw+dw
                if 0 <= nh2 < h and 0 <= nw2 < w and s[nh2][nw2] == "." and dist[nh2][nw2] == -1:
                    dist[nh2][nw2] = dist[nh][nw] + 1
                    q.append((nh2, nw2))
    print(dist[dh-1][dw-1])

=======
Suggestion 7

def main():
    # 入力
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]

    # 0-indexed
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1

    # 移動Aを行う場合の最短距離
    distA = [[-1] * W for _ in range(H)]
    distA[C_h][C_w] = 0

    # 移動Aを行うためのキュー
    queA = [(C_h, C_w)]

    # 移動Aを行う
    while queA:
        h, w = queA.pop(0)

        # 上下左右に移動
        for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nh = h + dh
            nw = w + dw

            # 移動先が迷路の外に出る場合は無視
            if not (0 <= nh < H and 0 <= nw < W):
                continue

            # 移動先が壁の場合は無視
            if S[nh][nw] == "#":
                continue

            # 移動先がすでに訪問済みの場合は無視
            if distA[nh][nw] != -1:
                continue

            # 移動先の距離を更新
            distA[nh][nw] = distA[h][w] + 1

            # キューに追加
            queA.append((nh, nw))

    # 移動Bを行う場合の最短距離
    distB = [[-1] * W for _ in range(H)]
    distB[C_h][C_w] = 0

    # 移動Bを行うためのキュー
    queB = [(C_h, C_w)]

    #

=======
Suggestion 8

def main():
    H,W = map(int,input().split())
    C_h,C_w = map(int,input().split())
    D_h,D_w = map(int,input().split())
    S = [list(input()) for _ in range(H)]

    # ワープ魔法の使用回数を求める
    # ワープ魔法は移動可能なマスにしか使用できない
    # そのため、BFSを用いて、移動可能なマスについてワープ魔法を使う回数を求める
    # また、移動可能なマスについては、ワープ魔法を使わずに移動することも可能である
    # そのため、移動可能なマスについては、ワープ魔法を使わずに移動する回数も求める

    # ワープ魔法を使わない回数を求める
    # ワープ魔法を使わない回数は、BFSを用いて、移動可能なマスについて、移動する回数を求める
    # ただし、移動可能なマスについては、ワープ魔法を使わない回数も求める
    # そのため、移動可能なマスについては、ワープ魔法を使わない回数とワープ魔法を使う回数の最小値を求める
    # また、移動可能なマスについては、移動する回数が最小値であるかどうかも判定する

    # 移動可能なマスについて、移動する回数が最小値であるかどうかを判定する
    # 移動可能なマスについて、ワープ魔法を使わない回数とワープ魔法

=======
Suggestion 9

def main():
    H,W = map(int,input().split())
    Ch,Cw = map(int,input().split())
    Dh,Dw = map(int,input().split())
    S = []
    for _ in range(H):
        S.append(list(input()))
    #print(H,W,Ch,Cw,Dh,Dw,S)

    #最短距離を求める
    #ワープ魔法で到達できる場合は、それを優先する
    #ワープ魔法で到達できない場合は、移動Aを優先する
    #ワープ魔法で到達できない場合は、移動Bを優先する

    #ワープ魔法の範囲
    warp = 2
    #ワープ魔法で移動するときの移動コスト
    warp_cost = 1
    #移動Aで移動するときの移動コスト
    moveA_cost = 1
    #移動Bで移動するときの移動コスト
    moveB_cost = 1

    #移動可能なマスのリスト
    move_list = []
    #ワープ魔法で移動可能なマスのリスト
    warp_list = []

    #ワープ魔法で移動可能なマスをリストに追加
    for i in range(1,H+1):
        for j in range(1,W+1):
            if abs(i-Ch) <= warp and abs(j-Cw) <= warp and S[i-1][j-1] == ".":
                warp_list.append([i,j])

    #print(warp_list)

    #移動可能なマスのリストを作成
    for i in range(1,H+1):
        for j in range(1,W+1):
            if S[i-1][j-1] == ".":
                move_list.append([i,j])

    #print(move_list)

    #最短距離を求める
    #ワープ魔法で

=======
Suggestion 10

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    H,W = map(int,input().split())
    Ch,Cw = map(int,input().split())
    Dh,Dw = map(int,input().split())
    S = [input() for _ in range(H)]

    #壁の場合は-1を代入
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                S[i] = S[i][:j] + '-1' + S[i][j+1:]
    S = [list(map(int,s.split())) for s in S]

    #初期化
    que = deque()
    for i in range(H):
        for j in range(W):
            if i == Ch-1 and j == Cw-1:
                S[i][j] = 0
                que.append((i,j))
            else:
                S[i][j] = -1
    #bfs
    while que:
        y,x = que.popleft()
        #移動A
        for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
            if 0 <= y+i < H and 0 <= x+j < W:
                if S[y+i][x+j] == -1:
                    S[y+i][x+j] = S[y][x]
                    que.appendleft((y+i,x+j))
        #移動B
        for i,j in ((-2,-2),(-2,-1),(-2,0),(-2,1),(-2,2),
                    (-1,-2),(-1,-1),(-1,0),(-1,1),(-1,2),
                    (0,-2),(0,-1),(0,0),(0,1),(0,2),
                    (1,-2),(1,-1),(1,0),(1,1),(1,2),
                    (2,-2),(2,-1),(2,0),(2,1),(2,2)):
            if 0 <= y+i < H and 0 <= x+j < W:
                if S[y+i][x+j] == -1:
                    S[y+i][x+j] = S[y][x] + 1
                    que.append((y+i,x+j))
    #print(S
