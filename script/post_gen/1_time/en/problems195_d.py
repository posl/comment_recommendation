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
        available = X[:L-1] + X[R:]
        available.sort()
        available = available[::-1]
        #print(available)
        used = [False] * N
        ans = 0
        for x in available:
            max_v = 0
            max_i = -1
            for j in range(N):
                if not used[j] and W[j] <= x and V[j] > max_v:
                    max_v = V[j]
                    max_i = j
            if max_i != -1:
                used[max_i] = True
                ans += V[max_i]
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
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X2 = X[:L-1] + X[R:]
        X2.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X2)):
                if X2[k] >= W[j]:
                    ans += V[j]
                    X2[k] = 0
                    break
        print(ans)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X1 = X[:L-1] + X[R:]
        X1.sort()
        V1 = [0] * N
        for j in range(N):
            for k in range(len(X1)):
                if X1[k] >= W[j]:
                    V1[j] = V[j]
                    X1[k] = 0
                    break
        print(sum(V1))

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
    for _ in range(Q):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        x = [0] * (M - (R - L + 1))
        cnt = 0
        for i in range(M):
            if i < L or i > R:
                x[cnt] = X[i]
                cnt += 1
        x.sort()
        v = [0] * N
        for i in range(N):
            for j in range(M - (R - L + 1)):
                if x[j] >= W[i]:
                    v[i] = V[i]
                    x[j] = 0
                    break
        print(sum(v))

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        available = X[:L-1] + X[R:]
        available.sort()
        available.reverse()
        available = [0] + available
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, M+1):
                if W[i-1] <= available[j]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + V[i-1])
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp[N][M])

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        A = X[:L-1] + X[R:]
        A.sort()
        ans = 0
        for j in range(N):
            for k in range(len(A)):
                if W[j] <= A[k]:
                    ans += V[j]
                    A[k] = -1
                    break
        print(ans)

=======
Suggestion 7

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
        X2 = X[:L - 1] + X[R:]
        X2.sort()
        V2 = sorted(zip(V, W), reverse=True)
        ans = 0
        for v, w in V2:
            for j in range(len(X2)):
                if X2[j] >= w:
                    ans += v
                    X2[j] = 0
                    break
        print(ans)

=======
Suggestion 8

def solve():
    N, M, Q = map(int, input().split())
    W = [0] * (N + 1)
    V = [0] * (N + 1)
    for i in range(1, N + 1):
        W[i], V[i] = map(int, input().split())
    X = [0] * (M + 1)
    for i in range(1, M + 1):
        X[i] = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        X_ = [0] * (M + 1)
        for i in range(1, M + 1):
            if i < L or R < i:
                X_[i] = X[i]
        dp = [0] * (sum(X_) + 1)
        for i in range(1, N + 1):
            for j in range(sum(X_), W[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - W[i]] + V[i])
        print(max(dp))

=======
Suggestion 9

def main():    
    N, M, Q = map(int, input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0] * M
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X_tmp = X[:L-1] + X[R:]
        X_tmp.sort()
        W_tmp = W[:]
        V_tmp = V[:]
        ans = 0
        for j in range(len(X_tmp)):
            max_idx = -1
            max_value = -1
            for k in range(len(W_tmp)):
                if W_tmp[k] <= X_tmp[j]:
                    if V_tmp[k] > max_value:
                        max_value = V_tmp[k]
                        max_idx = k
            if max_idx != -1:
                ans += V_tmp[max_idx]
                W_tmp.pop(max_idx)
                V_tmp.pop(max_idx)
        print(ans)

=======
Suggestion 10

def solve(N,M,Q,W,V,X,L,R):
    # Write your code here
    pass
