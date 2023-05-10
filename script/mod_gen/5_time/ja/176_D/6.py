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

if __name__ == '__main__':
    bfs()