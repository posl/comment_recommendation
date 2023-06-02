Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]
    for i in range(q):
        l,r = query[i]
        y = x[:l-1]+x[r:]
        y.sort()
        ans = 0
        for j in range(n):
            for k in range(len(y)):
                if wv[j][0]<=y[k]:
                    ans += wv[j][1]
                    y.pop(k)
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
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = X[:L - 1] + X[R:]
        N_ = len(X_)
        dp = [[0] * (sum(X_) + 1) for _ in range(N_ + 1)]
        for i in range(N_):
            for j in range(sum(X_) + 1):
                if j < X_[i]:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = max(dp[i][j], dp[i][j - X_[i]] + V[i])
        print(dp[-1][-1])

solve()

=======
Suggestion 3

def main():
    N,M,Q = map(int,input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    X = list(map(int,input().split()))
    for i in range(Q):
        L,R = map(int,input().split())
        X2 = X[:L-1] + X[R:]
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
Suggestion 4

def solve():
    N, M, Q = map(int, input().split())
    WV = [list(map(int, input().split())) for _ in range(N)]
    X = list(map(int, input().split()))
    Query = [list(map(int, input().split())) for _ in range(Q)]

    for L, R in Query:
        X_ = X[:L-1]+X[R:]
        X_.sort()
        WV_ = sorted(WV, key=lambda x: x[1], reverse=True)
        ans = 0
        for w, v in WV_:
            for i, x in enumerate(X_):
                if w <= x:
                    X_.pop(i)
                    ans += v
                    break
        print(ans)

=======
Suggestion 5

def solve():
    N,M,Q = map(int,input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    X = [0] * M
    X = list(map(int,input().split()))
    query = [0] * Q
    for i in range(Q):
        query[i] = list(map(int,input().split()))
    for i in range(Q):
        L = query[i][0]
        R = query[i][1]
        X1 = X[:L-1]
        X2 = X[R:]
        X1.extend(X2)
        X1.sort()
        X2 = X1
        X2 = X2[::-1]
        X1 = X1[::-1]
        X3 = X1[:N]
        X4 = X2[:N]
        ans = 0
        for j in range(1<<N):
            w = 0
            v = 0
            for k in range(N):
                if j & (1<<k):
                    w += W[k]
                    v += V[k]
            if w > X3[0]:
                continue
            if w <= X4[0]:
                ans = max(ans,v)
                continue
            l = 0
            r = N-1
            while r-l > 1:
                m = (l+r)//2
                if w <= X4[m]:
                    l = m
                else:
                    r = m
            ans = max(ans,v+X4[l+1]-w)
        print(ans)
solve()

=======
Suggestion 6

def main():
    n,m,q = map(int,input().split())
    wv = [list(map(int,input().split())) for _ in range(n)]
    x = list(map(int,input().split()))
    query = [list(map(int,input().split())) for _ in range(q)]

    ans = []

    for i in range(q):
        l,r = query[i][0],query[i][1]
        box = x[:l-1]+x[r:]
        box.sort()
        box.reverse()
        box = box[:n]
        box.sort()
        box.reverse()
        box = box[:n]
        wv.sort(key=lambda x:x[1])
        wv.reverse()
        wv = wv[:n]
        wv.sort(key=lambda x:x[0])
        wv.reverse()
        wv = wv[:n]
        wv = [i for i in wv if i[0]<=box[0]]
        wv.sort(key=lambda x:x[1])
        wv.reverse()
        wv = wv[:n]
        ans.append(sum([i[1] for i in wv]))

    for i in ans:
        print(i)

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    query = []
    for i in range(Q):
        l, r = map(int, input().split())
        query.append([l, r])
    for i in range(Q):
        l, r = query[i]
        X_copy = X.copy()
        del X_copy[l-1:r]
        X_copy.sort()
        W_copy = W.copy()
        V_copy = V.copy()
        ans = 0
        for j in range(N):
            for k in range(M-len(X_copy)):
                if W_copy[j] <= X_copy[k]:
                    ans += V_copy[j]
                    del W_copy[j]
                    del V_copy[j]
                    break
        print(ans)

=======
Suggestion 8

def max_value(w,v,x):
    dp = [[0 for i in range(x+1)] for j in range(len(w)+1)]
    for i in range(1,len(w)+1):
        for j in range(1,x+1):
            if j >= w[i-1]:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

n,m,q = map(int,input().split())
w,v = [],[]
for i in range(n):
    wi,vi = map(int,input().split())
    w.append(wi)
    v.append(vi)
x = list(map(int,input().split()))
query = []
for i in range(q):
    l,r = map(int,input().split())
    query.append([l,r])
for i in range(q):
    l,r = query[i]
    w1 = w[:l-1]+w[r:]
    v1 = v[:l-1]+v[r:]
    x1 = x[:]
    print(max_value(w1,v1,x1))

=======
Suggestion 9

def main():
    # N M Q = map(int, input().split())
    # print(N, M, Q)
    # W = []
    # V = []
    # for i in range(N):
    #     w, v = map(int, input().split())
    #     W.append(w)
    #     V.append(v)
    # print(W)
    # print(V)
    # X = list(map(int, input().split()))
    # print(X)
    # Q = int(input())
    # print(Q)
    # for i in range(Q):
    #     l, r = map(int, input().split())
    #     print(l, r)
    N = 3
    M = 4
    Q = 3
    W = [1, 5, 7]
    V = [9, 3, 8]
    X = [1, 8, 6, 9]
    Q = [[4, 4], [1, 4], [1, 3]]
    for i in range(Q):
        l = Q[i][0]
        r = Q[i][1]
        print(l, r)
        # for j in range(l, r+1):
        #     print(j)
        #     X[j-1] = 0
        # print(X)
        # X.sort()
        # print(X)
        # for j in range(N):
        #     for k in range(M):
        #         if W[j] <= X[k]:
        #             X[k] = 0
        #             break
        # print(X)
        # for j in range(M):
        #     if X[j] != 0:
        #         print(X[j])
        #         X[j] = 0
        #         break
        # print(X)
        # X.sort()
        # print(X)
        # for j in range(N):
        #     for k in range(M):
        #         if W[j] <= X[k]:
        #             X[k] = 0
        #             break
        # print(X)
        # for j in range(M):
        #     if X[j] != 0:
        #         print(X[j])
        #         X[j] = 0
        #         break
        # print(X)
        # X.sort()
        # print(X)

=======
Suggestion 10

def main():
    pass
