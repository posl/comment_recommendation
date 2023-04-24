Synthesizing 9/10 solutions

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
        X_tmp = X.copy()
        for j in range(L-1, R):
            X_tmp[j] = -1
        X_tmp.sort()
        W_tmp = W.copy()
        V_tmp = V.copy()
        for j in range(M):
            if X_tmp[j] == -1:
                continue
            for k in range(N):
                if W_tmp[k] > X_tmp[j]:
                    W_tmp[k] = -1
                    V_tmp[k] = -1
        W_tmp.sort()
        V_tmp.sort()
        ans = 0
        for j in range(N):
            if W_tmp[j] == -1:
                continue
            for k in range(N):
                if W_tmp[j] <= W[k] and V_tmp[N-1-k] != -1:
                    ans += V_tmp[N-1-k]
                    W_tmp[j] = -1
                    V_tmp[N-1-k] = -1
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
    for _ in range(Q):
        L, R = map(int, input().split())
        #print(L, R)
        #print(X)
        #print(W)
        #print(V)
        #print()

        # 箱を選ぶ
        box = X[:L - 1] + X[R:]
        #print(box)
        #print()

        # 箱に入れる荷物を選ぶ
        # 箱の大きさでソートする
        box.sort()
        #print(box)
        #print()

        # 荷物を大きさでソートする
        W_V = sorted(zip(W, V), key=lambda x: x[0])
        #print(W_V)
        #print()

        # 荷物を箱に入れる
        value = 0
        for w, v in W_V:
            for i, b in enumerate(box):
                if w <= b:
                    value += v
                    box[i] = 0
                    break
        print(value)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        # ボールを箱に入れる
        # 重さの重複を許す
        # 価値の合計を最大化
        # 価値の合計が最大になるような箱の選び方を

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        #print(L, R)
        #箱を選ぶ
        box = X[:L-1] + X[R:]
        #print(box)
        #荷物を選ぶ
        wv = [[W[i], V[i]] for i in range(N)]
        #print(wv)
        #価値の高い順にソート
        wv.sort(key=lambda x: x[1], reverse=True)
        #print(wv)
        #箱に入れる
        ans = 0
        for w, v in wv:
            #print(w, v)
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box[i] = 0
                    break
        print(ans)

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    X = [0] * M
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    for i in range(M):
        X[i] = int(input())
    for i in range(Q):
        L, R = map(int, input().split())
        used = [False] * M
        for j in range(L-1, R):
            used[j] = True
        box = []
        for j in range(M):
            if not used[j]:
                box.append(X[j])
        box.sort()
        w = W.copy()
        v = V.copy()
        for j in range(len(box)):
            for k in range(N):
                if w[k] <= box[j]:
                    w[k] = 0
                    v[k] = 0
        print(sum(v))

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    X = []
    for _ in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    for _ in range(M):
        x = int(input())
        X.append(x)
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L-1] + X[R:]
        X_.sort()
        X_.reverse()
        W_ = W[:]
        V_ = V[:]
        ans = 0
        for x in X_:
            w_max = 0
            v_max = 0
            for i in range(len(W_)):
                if W_[i] <= x:
                    if v_max < V_[i]:
                        w_max = W_[i]
                        v_max = V_[i]
                        index = i
            if v_max != 0:
                W_.pop(index)
                V_.pop(index)
                ans += v_max
        print(ans)

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for L, R in Query:
        #print(L, R)
        boxes = X[:L-1] + X[R:]
        boxes.sort()
        #print(boxes)
        wv = WV[:]
        wv.sort(key=lambda x:x[1], reverse=True)
        #print(wv)
        ans = 0
        for w, v in wv:
            for i, b in enumerate(boxes):
                if w <= b:
                    ans += v
                    boxes[i] = 0
                    break
        print(ans)

=======
Suggestion 8

def main():
    N,M,Q = map(int,input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    X = [0] * M
    X = list(map(int,input().split()))
    Query = []
    for i in range(Q):
        L,R = map(int,input().split())
        Query.append([L,R])
    for i in range(Q):
        L,R = Query[i]
        L -= 1
        R -= 1
        tmp = X[:L] + X[R+1:]
        tmp.sort(reverse = True)
        w = []
        v = []
        for j in range(N):
            if W[j] <= tmp[0]:
                w.append(W[j])
                v.append(V[j])
        dp = [[0 for j in range(len(tmp))] for k in range(len(w)+1)]
        for j in range(1,len(w)+1):
            for k in range(len(tmp)):
                if w[j-1] <= tmp[k]:
                    dp[j][k] = max(dp[j-1][k],dp[j-1][k-w[j-1]]+v[j-1])
                else:
                    dp[j][k] = dp[j-1][k]
        print(dp[-1][-1])

=======
Suggestion 9

def solve():
    N,M,Q = map(int,input().split())
    W = [0]*N
    V = [0]*N
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    X = [0]*M
    for i in range(M):
        X[i] = int(input())
    query = [0]*Q
    for i in range(Q):
        L,R = map(int,input().split())
        L -= 1
        R -= 1
        query[i] = (L,R)
    for L,R in query:
        #箱の大きさのリストを作る
        x = []
        for i in range(M):
            if i < L or R < i:
                x.append(X[i])
        #箱の大きさのリストを使って、各荷物の価値の合計の最大値を求める
        dp = [0]*(sum(x)+1)
        for i in range(N):
            for j in range(sum(x),W[i]-1,-1):
                dp[j] = max(dp[j],dp[j-W[i]]+V[i])
        print(max(dp))

solve()
