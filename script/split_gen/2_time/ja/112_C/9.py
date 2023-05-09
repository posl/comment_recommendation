def main():
    N = int(input())
    # 高さが0でない座標を取得
    pos = []
    for i in range(N):
        x, y, h = map(int, input().split())
        if h > 0:
            pos.append((x, y, h))
    # 高さが0でない座標が1つの場合は、その座標を出力
    if len(pos) == 1:
        print(pos[0][0], pos[0][1], pos[0][2])
        return
    # 高さが0でない座標が2つ以上の場合は、全探索
    for cx in range(101):
        for cy in range(101):
            h = pos[0][2] + abs(pos[0][0] - cx) + abs(pos[0][1] - cy)
            for i in range(1, len(pos)):
                if h - abs(pos[i][0] - cx) - abs(pos[i][1] - cy) != pos[i][2]:
                    break
            else:
                print(cx, cy, h)
                return
