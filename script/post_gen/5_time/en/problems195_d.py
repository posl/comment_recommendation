Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
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
            for j in range(len(X_)-1, -1, -1):
                if W[i] <= X_[j]:
                    ans += V[i]
                    X_.pop(j)
                    break
        print(ans)

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    W = [0]*N
    V = [0]*N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L-1] + X[R:]
        X_.sort()
        ans = 0
        for j in range(N):
            for k in range(M-L-R+1):
                if W[j] <= X_[k]:
                    ans += V[j]
                    X_.pop(k)
                    break
        print(ans)

=======
Suggestion 3

def solve():
    N,M,Q=map(int,input().split())
    W=[0]*N
    V=[0]*N
    for i in range(N):
        W[i],V[i]=map(int,input().split())
    X=list(map(int,input().split()))
    for i in range(Q):
        L,R=map(int,input().split())
        X_=X[:L-1]+X[R:]
        X_.sort()
        ans=0
        for j in range(N):
            for k in range(len(X_)-1,-1,-1):
                if X_[k]>=W[j]:
                    ans+=V[j]
                    X_.pop(k)
                    break
        print(ans)
solve()

=======
Suggestion 4

def solve():
    n, m, q = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    query = [tuple(map(int, input().split())) for _ in range(q)]

    wv.sort(key=lambda x: -x[1])
    x = sorted([(i, j) for i, j in enumerate(x)], key=lambda x: x[1])
    for l, r in query:
        box = x[:l-1] + x[r:]
        box.sort(key=lambda x: x[0])
        ans = 0
        for i, j in wv:
            for k in range(len(box)):
                if box[k][1] >= i:
                    box.pop(k)
                    break
            else:
                continue
            ans += j
        print(ans)

=======
Suggestion 5

def solve():
    N,M,Q = map(int,input().split())
    WV = [list(map(int,input().split())) for _ in range(N)]
    WV.sort(key=lambda x:x[1],reverse=True)
    X = list(map(int,input().split()))
    for _ in range(Q):
        L,R = map(int,input().split())
        X_ = X[:L-1]+X[R:]
        X_.sort()
        ans = 0
        for w,v in WV:
            for i in range(len(X_)):
                if X_[i]>=w:
                    ans += v
                    X_.pop(i)
                    break
        print(ans)

=======
Suggestion 6

def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    queries = [list(map(int,input().split())) for _ in range(q)]

    for i in range(q):
        l,r = queries[i]
        boxes = x[:l-1] + x[r:]
        boxes.sort()
        #print(boxes)
        tmp = 0
        for j in range(n):
            for k in range(len(boxes)):
                if wv[j][0] <= boxes[k]:
                    tmp += wv[j][1]
                    boxes.pop(k)
                    break
        print(tmp)

=======
Suggestion 7

def get_input():
    n, m, q = map(int, input().split())
    wv = []
    for _ in range(n):
        wv.append(list(map(int, input().split())))
    x = list(map(int, input().split()))
    query = []
    for _ in range(q):
        query.append(list(map(int, input().split())))
    return n, m, q, wv, x, query

=======
Suggestion 8

def solve():
    N,M,Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    W = [w for w,v in WV]
    V = [v for w,v in WV]
    X = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]

    for query in queries:
        L,R = query
        boxes = X[:L-1] + X[R:]
        boxes.sort()

        ans = 0
        for box in boxes:
            for i in range(N):
                if W[i] <= box:
                    ans += V[i]
                    W[i] = 10**9
                    break
        print(ans)

=======
Suggestion 9

def solve():
    N,M,Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    WV = sorted(WV, key=lambda x: (x[1], x[0]), reverse=True)
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]
    for L,R in Query:
        X_ = X[:L-1] + X[R:]
        X_ = sorted(X_)
        ans = 0
        for w,v in WV:
            for i in range(len(X_)):
                if X_[i] >= w:
                    ans += v
                    X_.pop(i)
                    break
        print(ans)

solve()

=======
Suggestion 10

def max_value(baggage, boxes):
    #print(baggage, boxes)
    if len(baggage) == 0 or len(boxes) == 0:
        return 0
    if baggage[0][0] <= boxes[0][0]:
        return max(baggage[0][1] + max_value(baggage[1:], boxes[1:]), max_value(baggage[1:], boxes))
    else:
        return max_value(baggage[1:], boxes)
