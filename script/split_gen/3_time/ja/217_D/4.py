def main():
    L, Q = map(int, input().split())
    # 木材の長さを管理するリスト
    wood = [L]
    # クエリを処理する
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            # 木材を切る
            wood = cut_wood(wood, x)
        else:
            # 木材の長さを出力する
            print(get_wood(wood, x))
