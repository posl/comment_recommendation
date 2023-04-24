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
        L -= 1
        R -= 1
        #print(N, M, Q)
        #print(W)
        #print(V)
        #print(X)
        #print(L, R)
        #print()
        W2 = W[:]
        V2 = V[:]
        X2 = X[:]
        del W2[L:R+1]
        del V2[L:R+1]
        del X2[L:R+1]
        #print(W2)
        #print(V2)
        #print(X2)
        #print()
        V2, W2 = zip(*sorted(zip(V2, W2), reverse=True))
        #print(W2)
        #print(V2)
        #print()
        ans = 0
        for i in range(len(X2)):
            for j in range(len(W2)):
                if W2[j] <= X2[i]:
                    ans += V2[j]
                    X2[i] = 0
                    W2[j] = 10**6 + 1
                    break
        print(ans)

main()

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
    for i in range(Q):
        L, R = map(int, input().split())
        #print("L, R", L, R)
        X2 = X[:L-1] + X[R:]
        X2.sort()
        #print("X2", X2)
        W2 = W[:]
        V2 = V[:]
        for j in range(M - R + L - 1):
            for k in range(N):
                if W2[k] <= X2[j]:
                    W2[k] = 0
                    V2[k] = 0
        #print("W2", W2)
        #print("V2", V2)
        ans = 0
        for j in range(N):
            ans += V2[j]
        print(ans)

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
    for q in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        x = X[:L] + X[R + 1:]
        x.sort()
        v = [0] * N
        for i in range(N):
            for j in range(len(x)):
                if x[j] >= W[i]:
                    v[i] = V[i]
                    x[j] = 0
                    break
        print(sum(v))

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
        #print(L, R)
        X_ = X[0:L-1] + X[R:]
        #print(X_)
        ans = 0
        for j in range(2 ** N):
            s = 0
            v = 0
            for k in range(N):
                if (j >> k) & 1:
                    s += W[k]
                    v += V[k]
            for x in X_:
                if s <= x:
                    ans = max(ans, v)
                    break
        print(ans)

=======
Suggestion 5

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
        L -= 1
        R -= 1
        #print(L, R)
        X2 = X.copy()
        for j in range(L, R+1):
            X2[j] = -1
        #print(X2)
        X3 = []
        for j in range(M):
            if X2[j] != -1:
                X3.append(X2[j])
        #print(X3)
        ans = 0
        for j in range(N):
            for k in range(len(X3)):
                if W[j] <= X3[k]:
                    ans += V[j]
                    X3[k] = -1
                    break
        print(ans)
        #print()

=======
Suggestion 6

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
        #print(W, V, X, L, R)
        print(solve(N, M, Q, W, V, X, L, R))

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
    for i in range(Q):
        L, R = map(int, input().split())
        x = X[:L-1] + X[R:]
        x.sort()
        v = [0] * N
        for j in range(N):
            for k in range(M):
                if W[j] <= x[k]:
                    v[j] = V[j]
                    x[k] = 0
                    break
        print(sum(v))

=======
Suggestion 8

def main():
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
        boxes = X[:L-1] + X[R:]
        boxes.sort()
        w = []
        v = []
        for i in range(N):
            if W[i] <= boxes[-1]:
                w.append(W[i])
                v.append(V[i])
        dp = [[0]*(len(boxes)+1) for i in range(len(w)+1)]
        for i in range(len(w)):
            for j in range(len(boxes)):
                if w[i] <= boxes[j]:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + v[i])
                else:
                    dp[i+1][j+1] = dp[i][j+1]
        print(dp[-1][-1])

=======
Suggestion 9

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
        #print(N, M, Q)
        #print(W)
        #print(V)
        #print(X)
        #print(L, R)
        X_ = X[:L - 1] + X[R:]
        X_.sort()
        #print(X_)
        ans = 0
        for j in range(N):
            for k in range(len(X_)):
                if W[j] <= X_[k]:
                    ans += V[j]
                    X_[k] = 0
                    break
        print(ans)

=======
Suggestion 10

def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    X = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    for i in range(M):
        x = int(input())
        X.append(x)
    for i in range(Q):
        l, r = map(int, input().split())
        w = W
        v = V
        x = X
        w = w[l-1:r]
        v = v[l-1:r]
        x = x[l-1:r]
        print(w)
        print(v)
        print(x)
