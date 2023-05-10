def main():
    # L:木材の長さ
    # Q:クエリの数
    L, Q = map(int, input().split())
    # 木材の長さを保存する配列
    wood = [L]
    # クエリを保存する配列
    query = []
    # クエリの数だけループ
    for i in range(Q):
        # クエリを保存
        query.append(list(map(int, input().split())))
    # クエリを処理
    for i in range(Q):
        # クエリが1の場合
        if query[i][0] == 1:
            # 木材を分割
            wood = wood_division(wood, query[i][1])
        # クエリが2の場合
        elif query[i][0] == 2:
            # 木材の長さを出力
            print(wood_length(wood, query[i][1]))
