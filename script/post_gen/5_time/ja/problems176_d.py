Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    from sys import stdin
    input = stdin.readline
    h, w = map(int, input().split())
    ch, cw = map(int, input().split())
    dh, dw = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]
    from collections import deque
    q = deque([(ch - 1, cw - 1)])
    visited = [[False] * w for _ in range(h)]
    visited[ch - 1][cw - 1] = True
    d = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if i == dh - 1 and j == dw - 1:
                print(d)
                return
            for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w and s[ni][nj] == '.' and not visited[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj))
        d += 1
        for i in range(max(0, ch - 3), min(h, ch + 2)):
            for j in range(max(0, cw - 3), min(w, cw + 2)):
                if s[i][j] == '.' and not visited[i][j]:
                    visited[i][j] = True
                    q.append((i, j))
    print(-1)
solve()

=======
Suggestion 2

def main():
    h, w = map(int, input().split())
    c_h, c_w = map(int, input().split())
    d_h, d_w = map(int, input().split())
    s = []
    for i in range(h):
        s.append(input())
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1

    # print(h, w, c_h, c_w, d_h, d_w, s)

    # ワープ魔法を使う最小回数を出力せよ。(D_h,D_w) に到達不可能な場合、かわりに -1 と出力せよ。
    # 考え方：ワープ魔法を使う回数を増やすことを考える
    #        ワープ魔法を使う回数を増やすことによって、目的地にたどり着ける場合と、たどり着けない場合がある
    #        たどり着ける場合は、ワープ魔法を使う回数を増やすことを考える
    #        たどり着けない場合は、ワープ魔法を使う回数を減らすことを考える
    #        このようにして、最小のワープ魔法を使う回数を求める
    #        たどり着けない場合は、-1を出力する
    #        たどり着ける場合は、ワープ魔法を使う回数を増やすことを考える
    #        たどり着けない場合は、ワープ魔法を使う回数を減らすことを考える
    #        このようにして、最小のワープ魔法を使う回数を求める
    #        た

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1

    INF = 10**9
    dist = [[INF] * W for _ in range(H)]
    dist[C_h][C_w] = 0

    queue = [(C_h, C_w)]
    while queue:
        h, w = queue.pop(0)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if not (0 <= h + dh < H and 0 <= w + dw < W):
                continue
            if S[h + dh][w + dw] == '#':
                continue
            if dist[h][w] + 1 < dist[h + dh][w + dw]:
                dist[h + dh][w + dw] = dist[h][w] + 1
                queue.append((h + dh, w + dw))

    ans = dist[D_h][D_w]
    if ans == INF:
        ans = -1
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
    INF = 10 ** 9
    dist = [[INF] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    q = [(C_h, C_w)]
    while q:
        h, w = q.pop(0)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h + dh, w + dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if S[nh][nw] == "#":
                continue
            if dist[nh][nw] <= dist[h][w]:
                continue
            dist[nh][nw] = dist[h][w]
            q.append((nh, nw))
        for nh in range(max(0, h - 2), min(h + 3, H)):
            for nw in range(max(0, w - 2), min(w + 3, W)):
                if S[nh][nw] == "#":
                    continue
                if dist[nh][nw] <= dist[h][w] + 1:
                    continue
                dist[nh][nw] = dist[h][w] + 1
                q.append((nh, nw))
    print(-1 if dist[D_h][D_w] == INF else dist[D_h][D_w])

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())

    S = [list(input()) for _ in range(H)]

    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1

    # 4方向への移動
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]

    # 5x5の範囲内にある道のマスへワープ魔法で移動する
    # 5x5の範囲内にある道のマスへワープ魔法で移動する
    # ワープ魔法を使う最小回数を出力せよ。(D_h,D_w) に到達不可能な場合、かわりに -1 と出力せよ。
    # どのマスにも移動できない場合は-1を出力する
    # 4方向への移動
    # ワープ魔法を使う最小回数を出力せよ。(D_h,D_w) に到達不可能な場合、かわりに -1 と出力せよ。
    # どのマスにも移動できない場合は-1を出力する
    # 4方向への移動
    # ワープ魔法を使う最小回数を出力せよ。(D_h,D_w) に到達不可能な場合、かわりに -1 と出力せよ。
    # どのマスにも移動できない場合は-1を出力する
    # 4方向への移動
    # ワープ魔法を使う最小回数を出力せよ。(D_h,D_w) に到達不可能な場合、か

=======
Suggestion 6

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

    # 魔法使いの現在地をキューに入れる
    q = []
    q.append([C_h, C_w])
    # 魔法使いが移動した回数を記録する
    dist = [[-1 for i in range(W)] for j in range(H)]
    dist[C_h][C_w] = 0
    # 移動方向のベクトル
    dh = [1, 0, -1, 0]
    dw = [0, 1, 0, -1]

    while len(q) != 0:
        # キューの先頭を取り出す
        h, w = q.pop(0)
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の魔法使いの座標を (nh,nw) とする
            nh = h + dh[i]
            nw = w + dw[i]
            # 移動が可能かの判定と既に訪れたことがあるかの判定 (dist[nh][nw] != -1 なら訪れたことあり)
            if (0 <= nh and nh < H and 0 <= nw and nw < W and S[nh][nw] != '#' and dist[nh][nw] == -1):
                # 移動できるならキューに入れ、その点の距離を更新
                q.append([nh, nw])
                dist[nh][nw] = dist[h][w] + 1

    # 魔法使いが (D_h,D_w) に到達不可能
    if dist[D_h][D_w] == -1:
        print(-1

=======
Suggestion 7

def bfs():
    # スタート地点をキューに入れる
    queue = deque([(ch-1, cw-1)])
    # スタート地点を訪問済みにする
    visited[ch-1][cw-1] = 0
    # キューが空になるまでループ
    while queue:
        # キューの先頭を取得
        h, w = queue.popleft()
        # ゴールなら探索を終了
        if h == dh-1 and w == dw-1:
            break
        # 移動4方向をループ
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            # 移動後のマスの座標を計算
            nh, nw = h + dh, w + dw
            # 移動後のマスが迷路の範囲外ならスキップ
            if nh < 0 or nh >= H or nw < 0 or nw >= W:
                continue
            # 移動後のマスが壁マスならスキップ
            if S[nh][nw] == '#':
                continue
            # 移動後のマスが訪問済みならスキップ
            if visited[nh][nw] != -1:
                continue
            # 移動後のマスをキューに入れる
            queue.append((nh, nw))
            # 移動後のマスを訪問済みにする
            visited[nh][nw] = visited[h][w] + 1

    # ゴールへの最小移動回数を出力。ゴールにたどり着けない場合は -1 を出力
    print(visited[dh-1][dw-1])

from collections import deque

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    C_h, C_w = map(int, input().split())
    D_h, D_w = map(int, input().split())
    S = [input() for _ in range(H)]
    C_h -= 1
    C_w -= 1
    D_h -= 1
    D_w -= 1
    INF = 10 ** 18
    dist = [[INF] * W for _ in range(H)]
    dist[C_h][C_w] = 0
    que = [(C_h, C_w)]
    while que:
        h, w = que.pop(0)
        for dh, dw in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nh, nw = h + dh, w + dw
            if not (0 <= nh < H and 0 <= nw < W):
                continue
            if S[nh][nw] == "#":
                continue
            if dist[nh][nw] <= dist[h][w]:
                continue
            dist[nh][nw] = dist[h][w]
            que.append((nh, nw))
        for dh in range(-2, 3):
            for dw in range(-2, 3):
                nh, nw = h + dh, w + dw
                if not (0 <= nh < H and 0 <= nw < W):
                    continue
                if S[nh][nw] == "#":
                    continue
                if dist[nh][nw] <= dist[h][w] + 1:
                    continue
                dist[nh][nw] = dist[h][w] + 1
                que.append((nh, nw))
    ans = dist[D_h][D_w]
    if ans == INF:
        ans = -1
    print(ans)
main()

=======
Suggestion 9

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
    dist[C_h][C_w] = 0
    q = [(C_h, C_w)]
    while q:
        i, j = q.pop()
        for i2, j2 in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if not (0 <= i2 < H and 0 <= j2 < W):
                continue
            if S[i2][j2] == '#':
                continue
            if dist[i2][j2] != -1:
                continue
            dist[i2][j2] = dist[i][j] + 1
            q.append((i2, j2))
        for i2 in range(max(0, i-2), min(H, i+3)):
            for j2 in range(max(0, j-2), min(W, j+3)):
                if S[i2][j2] == '#':
                    continue
                if dist[i2][j2] != -1:
                    continue
                dist[i2][j2] = dist[i][j] + 1
                q.append((i2, j2))
    print(dist[D_h][D_w])

=======
Suggestion 10

def solve(h, w, c_h, c_w, d_h, d_w, s):
    INF = 10 ** 9
    dist = [[INF] * w for _ in range(h)]
    dist[c_h - 1][c_w - 1] = 0
    q = [(c_h - 1, c_w - 1)]
    while q:
        i, j = q.pop(0)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < h and 0 <= nj < w):
                continue
            if s[ni][nj] == "#":
                continue
            if dist[ni][nj] <= dist[i][j]:
                continue
            dist[ni][nj] = dist[i][j]
            q.append((ni, nj))
        for di in range(-2, 3):
            for dj in range(-2, 3):
                ni, nj = i + di, j + dj
                if not (0 <= ni < h and 0 <= nj < w):
                    continue
                if s[ni][nj] == "#":
                    continue
                if dist[ni][nj] <= dist[i][j] + 1:
                    continue
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist[d_h - 1][d_w - 1] if dist[d_h - 1][d_w - 1] < INF else -1

h, w = map(int, input().split())
c_h, c_w = map(int, input().split())
d_h, d_w = map(int, input().split())
s = [input() for _ in range(h)]
print(solve(h, w, c_h, c_w, d_h, d_w, s))
