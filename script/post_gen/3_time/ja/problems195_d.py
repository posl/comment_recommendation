Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        X2 = X[:L-1] + X[R:]
        X2.sort()
        W2 = W[:]
        V2 = V[:]
        ans = 0
        for j in range(len(X2)):
            for k in range(len(W2)):
                if W2[k] <= X2[j]:
                    W2[k] = 10**10
                    ans += V2[k]
                    break
        print(ans)

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    Query = [[0] * 2 for i in range(Q)]
    for i in range(Q):
        Query[i][0], Query[i][1] = map(int, input().split())
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X_copy = X.copy()
        X_copy[L - 1:R] = [0] * (R - L + 1)
        X_copy = [x for x in X_copy if x != 0]
        X_copy.sort()
        V_copy = V.copy()
        W_copy = W.copy()
        for j in range(len(X_copy)):
            for k in range(len(W_copy)):
                if W_copy[k] <= X_copy[j]:
                    V_copy[j] += V_copy[k]
                    W_copy[k] = 0
        print(sum(V_copy))

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        W_ = W.copy()
        V_ = V.copy()
        X_ = X.copy()
        for j in range(L - 1, R):
            X_[j] = 0
        ans = 0
        for j in range(M):
            if X_[j] == 0:
                continue
            max_ = 0
            for k in range(N):
                if W_[k] <= X_[j] and V_[k] > max_:
                    max_ = V_[k]
                    max_k = k
            ans += max_
            W_[max_k] = 0
            V_[max_k] = 0
        print(ans)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        boxes = X[:]
        for j in range(L-1, R):
            boxes[j] = 0
        boxes = [box for box in boxes if box > 0]
        boxes.sort()
        Ws = W[:]
        Vs = V[:]
        Ws.sort()
        Vs.sort()
        Ws.reverse()
        Vs.reverse()
        ans = 0
        for box in boxes:
            for j in range(N):
                if Ws[j] <= box:
                    ans += Vs[j]
                    Ws[j] = 10**6+1
                    Vs[j] = 0
                    break
        print(ans)

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(Q)]
    
    for L, R in query:
        #箱の大きさのリストを作成
        x = X[:L-1] + X[R:]
        #荷物の価値のリストを作成
        v = [i[1] for i in wv]
        #荷物の大きさのリストを作成
        w = [i[0] for i in wv]
        #箱の大きさのリストを小さい順に並べ替える
        x.sort()
        #荷物の大きさのリストを小さい順に並べ替える
        w.sort()
        #荷物の価値のリストを大きい順に並べ替える
        v.sort(reverse=True)
        
        #荷物の価値のリストの大きさを取得
        v_len = len(v)
        #箱の大きさのリストの大きさを取得
        x_len = len(x)
        
        #荷物の価値のリストの大きさが箱の大きさのリストの大きさより大きい場合、
        #箱の大きさのリストの大きさを荷物の価値のリストの大きさにする
        if v_len > x_len:
            v_len = x_len
        
        #荷物の価値のリストの大きさが0より大きい場合、
        if v_len > 0:
            #荷物の価値のリストの大きさ分繰り返す
            for i in range(v_len):
                #箱の大きさのリストの要素が荷物の大きさのリストの要素より小さい場合、
                if x[i

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(Q)]

    for l, r in query:
        box = X[:l-1] + X[r:]
        box.sort()
        wv.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for w, v in wv:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box[i] = -1
                    break
        print(ans)

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    # 荷物の大きさと価値
    wv = [list(map(int, input().split())) for _ in range(N)]
    # 箱の大きさ
    x = list(map(int, input().split()))
    # クエリ
    query = [list(map(int, input().split())) for _ in range(Q)]

    # 箱の大きさでソート
    x.sort()

    # クエリごとに処理
    for l, r in query:
        # 箱の大きさを取得
        x_tmp = x[:l-1] + x[r:]
        # 荷物の大きさと価値でソート
        wv.sort(key=lambda x: x[1], reverse=True)
        # 箱の大きさでソート
        x_tmp.sort()
        # 箱に入れられる荷物の価値の合計
        ans = 0
        # 荷物を箱に入れる
        for w, v in wv:
            for i in range(len(x_tmp)):
                # 箱に入れられる荷物の大きさより小さい場合
                if x_tmp[i] >= w:
                    # 箱に荷物を入れる
                    x_tmp[i] = -1
                    ans += v
                    break
        print(ans)

=======
Suggestion 8

def main():
    N, M, Q = map(int, input().split())
    # 荷物の大きさと価値
    wv = [list(map(int, input().split())) for _ in range(N)]
    # 箱の大きさ
    X = list(map(int, input().split()))
    # クエリ
    query = [list(map(int, input().split())) for _ in range(Q)]

    # 箱の大きさでソート
    X.sort()
    # 荷物の価値でソート
    wv.sort(key=lambda x: x[1], reverse=True)

    for L, R in query:
        # 使用可能な箱を取得
        box = X[:L-1] + X[R:]

        # 箱の大きさでソート
        box.sort()

        ans = 0
        # 荷物の価値が高い順に詰めていく
        for w, v in wv:
            # 箱がなくなったら終了
            if len(box) == 0:
                break

            # 荷物を詰める箱を探す
            for i, x in enumerate(box):
                if w <= x:
                    # 荷物を詰める箱が見つかったら、箱を削除
                    ans += v
                    del box[i]
                    break

        print(ans)

=======
Suggestion 9

def main():
    N, M, Q = map(int, input().split())
    # 荷物の大きさと価値
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    # 箱の大きさ
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    # クエリ
    Query = [[0] * 2 for _ in range(Q)]
    for i in range(Q):
        Query[i][0], Query[i][1] = map(int, input().split())

    for i in range(Q):
        # 箱の大きさのリスト
        X_list = [0] * (M + 1)
        for j in range(M):
            X_list[j] = X[j]
        # 箱の大きさをソート
        X_list.sort()
        # 箱の大きさのリストの中で使えない箱の大きさを0にする
        for j in range(Query[i][0] - 1, Query[i][1]):
            X_list[j] = 0
        # 箱の大きさのリストの中で使えない箱の大きさを削除
        X_list = list(filter(lambda x: x != 0, X_list))

        # 荷物の大きさと価値のリスト
        WV_list = [[0, 0]] * N
        for j in range(N):
            WV_list[j][0] = W[j]
            WV_list[j][1] = V[j]
        # 荷物の大きさと価値のリストをソート
        WV_list.sort(key=lambda x: x[1], reverse=True)

        ans = 0
        for j in range(N):
            for k in range(len(X_list)):
                if WV_list[j][0] <= X_list[k]:
                    ans += WV_list[j][1]
                    X_list[k] = 0
                    break

        print(ans)

=======
Suggestion 10

def solve(n, m, q, wv, x, query):
    # 価値の大きい順にソート
    wv.sort(key=lambda x: x[1], reverse=True)
    # 箱の大きさの小さい順にソート
    x.sort()
    for l, r in query:
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-1:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-2:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-3:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-4:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-5:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが大きい箱を除外
        x = x[:l-1] + x[r-6:]
        # 箱の大きさの小さい順にソート
        x.sort()
        # 箱の大きさが
