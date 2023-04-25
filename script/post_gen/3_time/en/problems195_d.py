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
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        Y = X[:L-1] + X[R:]
        Y.sort()
        ans = 0
        for j in range(N):
            for k in range(len(Y)):
                if Y[k] >= W[j]:
                    ans += V[j]
                    Y[k] = 0
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
    for i in range(Q):
        L, R = map(int, input().split())
        W2 = [0] * (M - (R - L + 1))
        V2 = [0] * (M - (R - L + 1))
        X2 = [0] * (M - (R - L + 1))
        j = 0
        for k in range(M):
            if k < L - 1 or k > R - 1:
                W2[j] = W[k]
                V2[j] = V[k]
                X2[j] = X[k]
                j += 1
        dp = [[0 for _ in range(sum(X2) + 1)] for _ in range(M - (R - L + 1) + 1)]
        for k in range(M - (R - L + 1)):
            for l in range(sum(X2) + 1):
                if l >= W2[k]:
                    dp[k + 1][l] = max(dp[k][l - W2[k]] + V2[k], dp[k][l])
                else:
                    dp[k + 1][l] = dp[k][l]
        print(dp[M - (R - L + 1)][sum(X2)])

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
        X_tmp = X[:L-1] + X[R:]
        X_tmp.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X_tmp)):
                if X_tmp[k] >= W[j]:
                    ans += V[j]
                    X_tmp[k] = 0
                    break
        print(ans)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    W = [0]*N
    V = [0]*N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    X = [0]*M
    X = list(map(int, input().split()))
    for i in range(Q):
        L, R = map(int, input().split())
        X2 = X[:L-1] + X[R:]
        X2.sort()
        V2 = [0]*N
        for j in range(N):
            for k in range(len(X2)):
                if X2[k] >= W[j]:
                    V2[j] = V[j]
                    X2[k] = 0
                    break
        print(sum(V2))

=======
Suggestion 5

def solve():
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
        #L,R = map(int, input().split())
        #L -= 1
        #R -= 1
        #print(L, R)
        #print(X)
        #print(W)
        #print(V)
        #print(X)
        #print(X[:L-1])
        #print(X[R:])
        #print(X[:L-1] + X[R:])
        X2 = X[:L-1] + X[R:]
        #print(X2)
        X3 = sorted(X2, reverse=True)
        #print(X3)
        W2 = sorted(W, reverse=True)
        #print(W2)
        V2 = sorted(V, reverse=True)
        #print(V2)
        ans = 0
        for i in range(len(X3)):
            for j in range(len(W2)):
                if X3[i] >= W2[j]:
                    ans += V2[j]
                    break
        print(ans)
solve()

=======
Suggestion 6

def solve():
    N, M, Q = map(int, input().split())
    W = [0] + list(map(int, input().split()))
    V = [0] + list(map(int, input().split()))
    X = [0] + list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        A = [0] + [1] * M
        for i in range(L, R+1):
            A[i] = 0
        ans = 0
        for i in range(1, N+1):
            for j in range(1, M+1):
                if A[j] == 1 and X[j] >= W[i]:
                    ans += V[i]
                    A[j] = 0
                    break
        print(ans)
solve()

=======
Suggestion 7

def solve(N, M, Q, W, V, X, L, R):
    pass

N, M, Q = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
X = list(map(int, input().split()))
L = []
R = []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
for ans in solve(N, M, Q, W, V, X, L, R):
    print(ans)

The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of a single line with two integers N and K, the number of houses and the number of people, respectively.

The second line of the input gives the value of N integers P_1, P_2, ..., P_N, the prices of the houses.

Output

For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is the minimum possible total price, and z is the maximum possible total price.

Limits

Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ N ≤ 100.
1 ≤ K ≤ N.
1 ≤ P_i ≤ 10000, for all i.

Test set 1

K = 1.

Test set 2

No additional constraints.

Sample

Input

Output

3
4 1
100 300 200 400
4 2
100 300 200 400
4 4
100 300 200 400

Case #1: 100 100
Case #2: 300 500
Case #3: 400 400

In Sample Case #1, there is only one person, so they have to buy the house with the lowest price, 100.

In Sample Case #2, the first person buys the house with the lowest price, 100, and the second person buys the house with the second lowest price, 200.

In Sample Case #3, each person buys the house with the lowest price, 100.

=======
Suggestion 8

def getWV(N):
    wv = []
    for i in range(N):
        w, v = map(int, input().split())
        wv.append((w, v))
    return wv

=======
Suggestion 9

def solve(n,m,q,w,v,x,l,r):
    ans = []
    for i in range(q):
        ans.append(0)
        for j in range(l[i],r[i]+1):
            x[j-1] = 0
        for j in range(1,2**n):
            sumv = 0
            sumw = 0
            for k in range(n):
                if (j >> k) & 1:
                    sumv += v[k]
                    sumw += w[k]
            if sumw <= x[j-1]:
                ans[i] = max(ans[i],sumv)
        for j in range(l[i],r[i]+1):
            x[j-1] = 1
    return ans

=======
Suggestion 10

def solve(N, M, Q, W, V, X, L, R):
    # Write your code here
    return 0
