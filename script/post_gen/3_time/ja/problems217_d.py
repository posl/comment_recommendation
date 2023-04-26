Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    l = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            l.append(x)
        else:
            l.sort()
            print(l[bisect.bisect(l, x)] - l[bisect.bisect(l, x) - 1])

=======
Suggestion 2

def main():
    L, Q = map(int, input().split())
    line = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            line.append(x)
        elif c == 2:
            line.sort()
            for j in range(len(line)):
                if line[j] == x:
                    print(line[j+1] - line[j])
                    break

=======
Suggestion 3

def main():
    L, Q = map(int, input().split())
    d = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            d.append(x)
        else:
            d.sort()
            for j in range(len(d)):
                if d[j] == x:
                    print(d[j + 1] - d[j])
                    break

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    L = [N]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            L.append(x)
        else:
            L.sort()
            print(L[bisect.bisect_left(L, x)] - L[bisect.bisect_left(L, x) - 1])

=======
Suggestion 5

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

=======
Suggestion 6

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

=======
Suggestion 7

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

=======
Suggestion 8

def main():
    L, Q = map(int, input().split())
    # 木の長さ
    l = L
    # 切った場所
    cut = []
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            # 切られた場所のリストを昇順にソート
            cut.sort()
            # 切られた場所のリストの中に、xがある場合
            if x in cut:
                # xのインデックスを取得
                index = cut.index(x)
                # 木の長さの計算
                # 1番目の場合
                if index == 0:
                    # 木の長さ = 切られた場所 - 0
                    l = cut[index] - 0
                # 最後の場合
                elif index == len(cut) - 1:
                    # 木の長さ = L - 最後の切られた場所
                    l = L - cut[index]
                # それ以外の場合
                else:
                    # 木の長さ = 切られた場所 - 前の切られた場所
                    l = cut[index] - cut[index - 1]
            # 切られた場所のリストの中に、xがない場合
            else:
                # 切られた場所のリストの中に、xより小さい値がある場合
                if min(cut) < x:
                    # xより小さい値の中で最大の値を取得
                    max_cut = max([i for i in cut if i < x])
                    # 木の長さ = x - 前の切られた場所
                    l = x - max_cut
                # 切られた場所のリストの中に、xより大きい値がある場合
                elif max(cut) > x:
                    # xより大きい値の中で最小の

=======
Suggestion 9

def main():
    L, Q = map(int, input().split())
    # 線の位置を格納するリストを作成
    line_list = [0, L]
    # クエリに対する処理
    for i in range(Q):
        c_i, x_i = map(int, input().split())
        # 線を引く場合
        if c_i == 1:
            line_list.append(x_i)
        # 線を引く場合
        elif c_i == 2:
            # 線の位置を昇順にソート
            line_list.sort()
            # 線の位置の中で、線を引く位置よりも大きい値の最小のインデックスを取得
            index = line_list.index(x_i)
            # 線を引く位置よりも小さい値と大きい値の差を出力
            print(line_list[index] - line_list[index-1])

=======
Suggestion 10

def main():
    L, Q = map(int, input().split())
    # print(L, Q)
    # print()
    # print()

    # 木材の長さ
    # 木材の左端からの位置
    # 木材の右端からの位置
    # 木材��
