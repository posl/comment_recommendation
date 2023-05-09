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
