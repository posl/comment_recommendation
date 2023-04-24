Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    L, Q = map(int, input().split())
    C = []
    X = []
    for i in range(Q):
        c, x = map(int, input().split())
        C.append(c)
        X.append(x)

    #木材の長さを格納するリスト
    wood = [L]
    #木材の長さの累積和を格納するリスト
    wood_sum = [0]
    for i in range(Q):
        if C[i] == 1:
            #木材の長さの累積和を計算
            #木材の長さの累積和は木材の長さのリストの累積和
            #木材の長さのリストの累積和は木材の長さの累積和を計算するために必要
            wood_sum.append(wood_sum[-1] + wood[-1])
            #木材の長さを更新
            #木材の長さのリストの累積和を計算するために必要
            #木材の長さのリストの累積和は木材の長さの累積和を計算するために必要
            #木材の長さの累積和を計算するために必要
            wood.append(X[i] - (wood_sum[-1] - wood_sum[-2]))
            #木材の長さを更新
            #木材の長さのリストの累積和を計算するために必要
            #木材の長さの累積和を計算するために必要
            wood.append(wood_sum[-1] + wood[-2] - X[i])
        elif C[i] == 2:
            #木材の長さの累積和を計算
            #木材の長さの累積和は木材の長さのリストの累積和

=======
Suggestion 2

def main():
    L, Q = map(int, input().split())
    cut = [0, L]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            cut.sort()
            for j in range(len(cut)):
                if cut[j] == x:
                    print(cut[j + 1] - cut[j - 1])
                    break

=======
Suggestion 3

def main():
    L, Q = map(int, input().split())
    cut = []
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut.append(x)
        else:
            l = 0
            r = len(cut)
            while r - l > 1:
                m = (l + r) // 2
                if cut[m] < x:
                    l = m
                else:
                    r = m
            if cut[l] < x:
                print(x - cut[l])
            else:
                print(x)

=======
Suggestion 4

def main():
    l, q = map(int, input().split())
    l_list = [l]
    for _ in range(q):
        c, x = map(int, input().split())
        if c == 1:
            for i, l_i in enumerate(l_list):
                if l_i > x:
                    l_list[i] = x
                    l_list.insert(i + 1, l_i - x)
                    break
        else:
            for l_i in l_list:
                if l_i >= x:
                    print(l_i)
                    break

=======
Suggestion 5

def main():
    L, Q = map(int, input().split())
    # 木材の長さを格納するリスト
    wood = [L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            # 線 x がある地点で木材を 2 つに切る
            tmp = []
            for w in wood:
                if w > x:
                    tmp.append(w - x)
                    tmp.append(x)
                    wood.remove(w)
                    break
            wood += tmp
        else:
            # 線 x を含む木材を選び、その長さを出力する
            for w in wood:
                if w >= x:
                    print(w)
                    break

=======
Suggestion 6

def main():
    L, Q = map(int, input().split())
    #区間を管理するリスト
    interval_list = [(0, L)]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            for i in range(len(interval_list)):
                #区間の左端がxより小さく、区間の右端がxより大きい場合
                if interval_list[i][0] < x and interval_list[i][1] > x:
                    #区間を分割し、interval_listに格納する
                    interval_list.append((interval_list[i][0], x))
                    interval_list.append((x, interval_list[i][1]))
                    #分割した区間を削除する
                    interval_list.pop(i)
                    break
        else:
            for i in range(len(interval_list)):
                #区間の左端がxより小さく、区間の右端がxより大きい場合
                if interval_list[i][0] < x and interval_list[i][1] > x:
                    #区間の長さを出力する
                    print(interval_list[i][1] - interval_list[i][0])
                    break

=======
Suggestion 7

def main():
    L, Q = map(int, input().split())
    # 木材の長さを入れるリスト
    wood = [L]
    # クエリの処理
    for _ in range(Q):
        c, x = map(int, input().split())
        # 木材の切り分け
        if c == 1:
            wood.append(x)
            wood.append(L - x)
            wood.sort()
            L = wood[-1]
        # 木材の長さを出力
        else:
            for i in range(len(wood)):
                if wood[i] >= x:
                    print(wood[i])
                    break

=======
Suggestion 8

def main():
    L, Q = map(int, input().split())
    # クエリの種類と位置を格納する
    query = [list(map(int, input().split())) for _ in range(Q)]
    # 木の長さを格納する
    wood = [L]
    for i in range(Q):
        # クエリの種類が2のとき
        if query[i][0] == 2:
            # 木の長さを出力する
            print(wood[query[i][1] - 1])
        # クエリの種類が1のとき
        else:
            # 木の長さを更新する
            wood = update(wood, query[i][1])
    return

=======
Suggestion 9

def main():
    L,Q = map(int,input().split())
    #木材の長さ
    length = [L]
    #木材の開始位置
    start = [0]
    #クエリの処理
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            #木材の長さの更新
            for j in range(len(length)):
                if start[j] <= x < start[j] + length[j]:
                    length[j] = x - start[j]
                    start.insert(j+1,x)
                    length.insert(j+1,start[j+1] + length[j+1] - x)
                    break
        else:
            #木材の長さの出力
            for j in range(len(length)):
                if start[j] <= x < start[j] + length[j]:
                    print(length[j])
                    break

=======
Suggestion 10

def main():
    import sys
    input = sys.stdin.readline
    L, Q = map(int, input().split())
    # 始点と終点を記録
    # 貪欲法で木材を切る
    # 始点と終点の間の距離を出力
    # 木材を切るときは、始点と終点の間の距離を記録しておく
    # 木材を切ったら、木材の始点と終点の間の距離が記録されているので、
    # その距離を出力する
    # 木材の始点と終点を記録
    # 木材の始点と終点の間の距離を記録
    # 木材の始点と終点の間の距離を出力
    # 木材の始点と終点の間の距離を記録
    # 木材の始点と終点の間の距離を出力
    # 木材の始点と終点の間の距離を記録
    # 木材の始点と終点の間の距離を出力
    # 木材の始点と終点の間の距離を記録
    # 木材の始点と終点の間の距離を出力
    # 木材の始点と終点の間の距離を記録
    # 木材の始点と終点の間の距離を出力
    # 木材の始点と終点の間の距離を記録
    # 木材の始点と終点の間の距離を出力
    # 木材の始点と終点の間の距離
