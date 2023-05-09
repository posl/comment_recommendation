def main():
    L, Q = map(int, input().split())
    # 木材の長さ
    wood = [L]
    # 線の位置
    lines = []
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            # 線を引く
            lines.append(x)
            # 線の位置を基準に木材を分割
            wood = split_wood(wood, x)
        else:
            # 線を含む木材の長さを求める
            print(find_wood(wood, x))
