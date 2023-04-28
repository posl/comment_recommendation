Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    Query = [0] * Q
    for i in range(Q):
        Query[i] = list(map(int, input().split()))
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X2 = []
        for j in range(L-1):
            X2.append(X[j])
        for j in range(R, M):
            X2.append(X[j])
        X2.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X2)):
                if W[j] <= X2[k]:
                    ans += V[j]
                    X2.pop(k)
                    break
        print(ans)

=======
Suggestion 2

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
        box = X[:L-1] + X[R:]
        box.sort()
        ans = 0
        for i in range(N):
            for j in range(len(box)):
                if W[i] <= box[j]:
                    ans += V[i]
                    box.pop(j)
                    break
        print(ans)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]

    WV.sort(key=lambda x: x[1], reverse=True)
    for i in range(Q):
        l = Query[i][0]
        r = Query[i][1]
        X_ = X[:l-1] + X[r:]
        X_.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X_)):
                if WV[j][0] <= X_[k]:
                    ans += WV[j][1]
                    X_.pop(k)
                    break
        print(ans)

=======
Suggestion 4

def main():
    N,M,Q = map(int,input().split())
    W = []
    V = []
    for i in range(N):
        w,v = map(int,input().split())
        W.append(w)
        V.append(v)
    X = list(map(int,input().split()))
    Query = []
    for i in range(Q):
        l,r = map(int,input().split())
        Query.append((l,r))
    for i in range(Q):
        l = Query[i][0]
        r = Query[i][1]
        X_copy = X.copy()
        X_copy.pop(l-1)
        X_copy.pop(r-1)
        X_copy.sort()
        ans = 0
        for j in range(N):
            for k in range(M-2):
                if W[j] <= X_copy[k]:
                    ans += V[j]
                    X_copy.pop(k)
                    break
        print(ans)

=======
Suggestion 5

def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    for i in range(q):
        l,r = query[i]
        boxes = x[:l-1] + x[r:]
        boxes.sort()
        ans = 0
        for j in range(n):
            tmp = 0
            for k in range(len(boxes)):
                if wv[j][0] <= boxes[k]:
                    if tmp < wv[j][1]:
                        tmp = wv[j][1]
            ans += tmp
        print(ans)

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    WV.sort(key=lambda x: x[1], reverse=True)
    X = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for _ in range(Q)]

    for L, R in queries:
        box = X[:L-1] + X[R:]
        box.sort()
        ans = 0
        for w, v in WV:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box.pop(i)
                    break
        print(ans)

=======
Suggestion 7

def main():
    N,M,Q = map(int,input().split())
    WV = [list(map(int,input().split())) for _ in range(N)]
    WV.sort(key=lambda x:x[1],reverse=True)
    X = list(map(int,input().split()))
    for _ in range(Q):
        L,R = map(int,input().split())
        box = X[:L-1] + X[R:]
        box.sort()
        ans = 0
        for w,v in WV:
            for i in range(len(box)):
                if box[i] >= w:
                    ans += v
                    box.pop(i)
                    break
        print(ans)

=======
Suggestion 8

def main():
    N, M, Q = map(int, input().split())
    WV = [tuple(map(int, input().split())) for _ in range(N)]
    WV.sort(key=lambda x: -x[1])
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L - 1] + X[R:]
        X_.sort()
        ans = 0
        for w, v in WV:
            for i, x in enumerate(X_):
                if w <= x:
                    del X_[i]
                    ans += v
                    break
        print(ans)

=======
Suggestion 9

def main():
    N,M,Q = map(int, input().split())
    W = [0]*(N+1)
    V = [0]*(N+1)
    for i in range(1,N+1):
        W[i],V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for i in range(Q)]

    for i in range(Q):
        L,R = Query[i]
        box = X[:L-1] + X[R:]
        box.sort()
        #print(box)
        used = [False]*(N+1)
        ans = 0
        for j in range(len(box)):
            max_v = 0
            max_i = 0
            for k in range(1,N+1):
                if used[k] == False and W[k] <= box[j] and max_v < V[k]:
                    max_v = V[k]
                    max_i = k
            if max_v > 0:
                used[max_i] = True
                ans += max_v
        print(ans)

=======
Suggestion 10

def solve():
    N,M,Q = map(int,input().split())
    WV = [list(map(int,input().split())) for _ in range(N)]
    WV.sort(key=lambda x: x[1],reverse=True)
    X = list(map(int,input().split()))

    for _ in range(Q):
        L,R = map(int,input().split())
        X_ = X[:L-1] + X[R:]
        X_.sort()
        ans = 0
        for w,v in WV:
            for i in range(len(X_)):
                if X_[i] >= w:
                    ans += v
                    X_.pop(i)
                    break
        print(ans)
    return 0
