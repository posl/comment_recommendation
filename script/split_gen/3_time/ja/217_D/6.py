def main():
    #入力
    L, Q = map(int, input().split())
    #クエリを格納するリスト
    queries = []
    #クエリを読み込む
    for i in range(Q):
        queries.append(list(map(int, input().split())))
    #木材の長さを格納するリスト
    wood = [L]
    #クエリを処理する
    for query in queries:
        #クエリのタイプ
        c = query[0]
        #クエリの値
        x = query[1]
        #木材の長さを格納するリスト
        wood_next = []
        #木材を処理する
        for w in wood:
            #木材の長さがクエリの値より小さい場合
            if w < x:
                wood_next.append(w)
            #木材の長さがクエリの値と同じ場合
            elif w == x:
                wood_next.append(w)
                wood_next.append(w)
            #木材の長さがクエリの値より大きい場合
            else:
                wood_next.append(x)
                wood_next.append(w - x)
        #木材の長さを更新する
        wood = wood_next
        #クエリのタイプが2の場合
        if c == 2:
            #木材の長さを出力する
            print(wood[0])
            #木材の長さを更新する
            wood.pop(0)
