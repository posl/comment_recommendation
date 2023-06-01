Synthesizing 9/10 solutions

=======
Suggestion 1

def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        ans = 0
        for i in range(M):
            if i < L or R < i:
                ans += X[i]
        dp = [0] * (sum(X) + 1)
        for i in range(N):
            for j in range(sum(X), W[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])
        ans += dp[sum(X)]
        print(ans)

=======
Suggestion 2

def solve():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        X_ = X[:L] + X[R+1:]
        X_.sort()
        ans = 0
        for j in range(1 << len(X_)):
            x = 0
            for k in range(len(X_)):
                if j >> k & 1:
                    x += X_[k]
            w = 0
            for k in range(N):
                if x >= W[k] and x <= X[k]:
                    w += V[k]
            ans = max(ans, w)
        print(ans)
solve()

=======
Suggestion 3

def main():
    N,M,Q=map(int,input().split())
    W=[]
    V=[]
    for i in range(N):
        w,v=map(int,input().split())
        W.append(w)
        V.append(v)
    X=list(map(int,input().split()))
    for i in range(Q):
        L,R=map(int,input().split())
        X1=X[:L-1]
        X2=X[R:]
        X1.extend(X2)
        X1.sort()
        ans=0
        for j in range(N):
            for k in range(len(X1)):
                if W[j]<=X1[k]:
                    ans+=V[j]
                    X1.remove(X1[k])
                    break
        print(ans)

main()

=======
Suggestion 4

def solve(n, m, q, w, v, x, l, r):
    #print(n, m, q, w, v, x, l, r)
    #print(w)
    #print(v)
    #print(x)
    #print(l)
    #print(r)
    #print('-----------------------------')
    #print(n, m, q, w, v, x, l, r)
    #print(w)
    #print(v)
    #print(x)
    #print(l)
    #print(r)
    #print('-----------------------------')
    #print(n, m, q, w, v, x, l, r)
    #print(w)
    #print(v)
    #print(x)
    #print(l)
    #print(r)
    #print('-----------------------------')
    #print(n, m, q, w, v, x, l, r)
    #print(w)
    #print(v)
    #print(x)
    #print(l)
    #print(r)
    #print('-----------------------------')
    #print(n, m, q, w, v, x, l, r)
    #print(w)
    #print(v)
    #print(x)
    #print(l)
    #print(r)
    #print('-----------------------------')
    #print(n, m, q, w, v, x, l, r)
    #print(w)
    #print(v)
    #print(x)
    #print(l)
    #print(r)
    #print('-----------------------------')
    #print(n, m, q, w, v, x, l, r)
    #print(w)
    #print(v)
    #print(x)
    #print(l)
    #print(r)
    #print('-----------------------------')
    #print(n, m, q, w, v, x, l, r)
    #print(w)
    #print(v)
    #print(x)
    #print(l)
    #print(r)
    #print('-----------------------------')
    #print(n, m, q, w, v, x, l, r)
    #print(w)
    #print(v)
    #print(x)
    #print(l)
    #print(r)

    #print('-----------------------------')

    #print(n, m, q, w, v, x, l, r)

    #print(w)

=======
Suggestion 5

def get_max_value(w, v, x, l, r):
    # 从l到r中选出最大的x
    max_x = x[l-1]
    for i in range(l, r):
        if x[i] > max_x:
            max_x = x[i]
    # 从w中选出最大的x
    max_w = w[0]
    for i in range(1, len(w)):
        if w[i] > max_w:
            max_w = w[i]

    # 如果最大的x比最大的w大，说明可以把所有的w放入箱子
    if max_x > max_w:
        return sum(v)
    else:
        # 如果最大的x比最大的w小，说明不能把所有的w放入箱子
        # 从w中选出最大的x，然后把这个w放入箱子
        max_x_index = w.index(max_w)
        new_w = w.copy()
        new_w[max_x_index] = max_x
        return sum(new_w)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def solve():
    n, m, q = map(int, input().split())
    wv = [tuple(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    query = [tuple(map(int, input().split())) for _ in range(q)]

    wv.sort(key=lambda x: x[1], reverse=True)

    for l, r in query:
        print(max_value(wv, x, l - 1, r))

=======
Suggestion 8

def solve():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        print(query(N, M, W, V, X, L, R))

=======
Suggestion 9

def solve():
    N, M, Q = map(int, input().split())
    wv = [[int(i) for i in input().split()] for _ in range(N)]
    x = [int(i) for i in input().split()]
    query = [[int(i) for i in input().split()] for _ in range(Q)]

    wv.sort(key=lambda x: x[1], reverse=True)
    x.sort()
    for ql, qr in query:
        box = x[:ql-1] + x[qr:]
        box.sort()
        ans = 0
        for w, v in wv:
            for i in range(len(box)):
                if w <= box[i]:
                    ans += v
                    del box[i]
                    break
        print(ans)
