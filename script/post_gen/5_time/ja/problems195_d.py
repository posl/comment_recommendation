Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M,Q = map(int,input().split())
    W = [0]*N
    V = [0]*N
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    X = list(map(int,input().split()))
    Query = [0]*Q
    for i in range(Q):
        Query[i] = list(map(int,input().split()))
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X2 = X[:L-1] + X[R:]
        X2.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X2)):
                if X2[k] >= W[j]:
                    ans += V[j]
                    X2.pop(k)
                    break
        print(ans)

=======
Suggestion 2

def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]

    for L, R in queries:
        boxes = X[:L-1] + X[R:]
        boxes.sort()
        used = [False] * N
        ans = 0
        for b in boxes:
            max_v = 0
            max_i = -1
            for i in range(N):
                if not used[i] and W[i] <= b and max_v < V[i]:
                    max_v = V[i]
                    max_i = i
            if max_i >= 0:
                used[max_i] = True
                ans += max_v
        print(ans)

=======
Suggestion 3

def main():
    N,M,Q = map(int,input().split())
    WV = [list(map(int,input().split())) for _ in range(N)]
    X = list(map(int,input().split()))
    Query = [list(map(int,input().split())) for _ in range(Q)]

    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X_new = X[:L-1] + X[R:]
        X_new.sort()

        ans = 0
        for j in range(N):
            for k in range(len(X_new)):
                if WV[j][0] <= X_new[k]:
                    ans += WV[j][1]
                    X_new.pop(k)
                    break

        print(ans)

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
        X_ = X[:L-1] + X[R:]
        X_.sort()
        ans = 0
        for i in range(N):
            for j in range(len(X_)):
                if W[i] <= X_[j]:
                    ans += V[i]
                    X_.pop(j)
                    break
        print(ans)

=======
Suggestion 5

def solve():
    N, M, Q = map(int, input().split())
    WV = [tuple(map(int, input().split())) for _ in range(N)]
    WV.sort(key=lambda x: x[1], reverse=True)
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L - 1] + X[R:]
        X_.sort()
        ans = 0
        for w, v in WV:
            for i, x in enumerate(X_):
                if w <= x:
                    ans += v
                    X_.pop(i)
                    break
        print(ans)

=======
Suggestion 6

def solve():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    for i in range(q):
        l,r = query[i]
        box = x[:l-1] + x[r:]
        box.sort()
        ans = 0
        for j in range(n):
            if len(box) == 0:
                break
            for k in range(len(box)):
                if wv[j][0] <= box[k]:
                    ans += wv[j][1]
                    box.pop(k)
                    break
        print(ans)
    return 0

=======
Suggestion 7

def solve():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]

    WV.sort(key=lambda x: x[1], reverse=True)
    X.sort(reverse=True)

    for L, R in Query:
        # L-1までの箱の中で価値が最大の荷物を探す
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱を探す
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる箱の中で価値が最大の荷物を探す
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる箱の中で価値が最大の荷物を入れられる箱の中で最も大きい箱を探す
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる箱の中で価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる
        # 価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物を入れる箱の中で価値が最大の荷物を入れられる箱の中で最も大きい箱に対応する荷物

=======
Suggestion 8

def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]

    for i in range(Q):
        ans = 0
        l = Query[i][0]
        r = Query[i][1]
        box = X[:l-1] + X[r:]
        box.sort()
        for j in range(N):
            for k in range(len(box)):
                if WV[j][0] <= box[k]:
                    ans += WV[j][1]
                    del box[k]
                    break
        print(ans)

=======
Suggestion 9

def main():
    N, M, Q = map(int, input().split())
    WV = [[0 for i in range(2)] for j in range(N)]
    for i in range(N):
        WV[i] = list(map(int, input().split()))
    X = list(map(int, input().split()))
    Query = [[0 for i in range(2)] for j in range(Q)]
    for i in range(Q):
        Query[i] = list(map(int, input().split()))
    #print(N, M, Q)
    #print(WV)
    #print(X)
    #print(Query)
    for i in range(Q):
        #print(Query[i][0])
        #print(Query[i][1])
        #print(X[Query[i][0]-1:Query[i][1]])
        #print(sorted(X[Query[i][0]-1:Query[i][1]]))
        X2 = sorted(X[Query[i][0]-1:Query[i][1]])
        #print(X2)
        #print(len(X2))
        #print(WV)
        #print(len(WV))
        #print(WV[0][0])
        #print(len(WV[0]))
        #print(WV[0][1])
        #print(len(WV[0][1]))
        #print(WV[0][1][0])
        #print(len(WV[0][1][0]))
        #print(WV[0][1][1])
        #print(len(WV[0][1][1]))
        #print(WV[1][0])
        #print(len(WV[1]))
        #print(WV[1][1][0])
        #print(len(WV[1][1][0]))
        #print(WV[1][1][1])
        #print(len(WV[1][1][1]))
        #print(WV[2][0])
        #print(len(WV[2]))
        #print(WV[2][1][0])
        #print(len(WV[2][1][0]))
        #print(WV[2][1][1])
        #print(len(WV[2][1][1]))
        #print(WV[3][0])
        #print(len(WV[3]))
        #print(WV[3][1][0])
        #print(len(WV[3][

=======
Suggestion 10

def main():
    N, M, Q = map(int, input().split())
    W = [0] * (N + 1)
    V = [0] * (N + 1)
    for i in range(1, N + 1):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    Q = [list(map(int, input().split())) for _ in range(Q)]

    for l, r in Q:
        boxes = X[:l - 1] + X[r:]
        boxes.sort()
        used = [False] * N
        ans = 0
        for b in boxes:
            idx = -1
            for i in range(N):
                if not used[i] and W[i + 1] <= b and (idx == -1 or V[idx + 1] < V[i + 1]):
                    idx = i
            if idx != -1:
                used[idx] = True
                ans += V[idx + 1]
        print(ans)
