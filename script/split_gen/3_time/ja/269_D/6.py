def main():
    N = int(input())
    # 座標を入力
    xy = [list(map(int, input().split())) for _ in range(N)]
    # 連結成分の個数
    cnt = 0
    # 連結成分のリスト
    group = [0] * N
    # 連結成分に属する座標のリスト
    group_xy = [[0, 0]] * N
    # 座標を1つずつ見ていく
    for i, (x, y) in enumerate(xy):
        # 連結成分に属する座標のリスト
        group_xy[i] = [x, y]
        # 座標が連結成分に属しているかどうか
        for j, (x2, y2) in enumerate(group_xy):
            # 連結成分に属している場合
            if abs(x - x2) <= 1 and abs(y - y2) <= 1:
                # 連結成分のリストに連結成分の番号を入れる
                group[i] = j
                # 連結成分のリストに連結成分の番号を入れる
                group[j] = j
    # 連結成分のリストを見ていく
    for i in group:
        # 連結成分の個数を数える
        if i == cnt:
            cnt += 1
    print(cnt)
