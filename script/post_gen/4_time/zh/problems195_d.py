Synthesizing 10/10 solutions

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
        for bit in range(1 << (R - L + 1)):
            w = 0
            v = 0
            for i in range(R - L + 1):
                if bit & (1 << i):
                    w += W[L + i]
                    v += V[L + i]
            for i in range(M):
                if w <= X[i]:
                    ans = max(ans, v)
        print(ans)

=======
Suggestion 2

def main():
    n, m, q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]
    for l, r in query:
        box = x[:l-1] + x[r:]
        box.sort()
        ans = 0
        for i in range(n):
            for j in range(len(box)):
                if wv[i][0] <= box[j]:
                    ans += wv[i][1]
                    box.pop(j)
                    break
        print(ans)
main()

=======
Suggestion 3

def solve(n,m,q,w,v,x,query):
    ans = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[j-1]>=w[i-1] and query[0]<=j<=query[1]:
                ans = max(ans,v[i-1])
    return ans

=======
Suggestion 4

def solve():
    N,M,Q=map(int,input().split())
    W=[]
    V=[]
    for _ in range(N):
        w,v=map(int,input().split())
        W.append(w)
        V.append(v)
    X=list(map(int,input().split()))
    Query=[]
    for _ in range(Q):
        l,r=map(int,input().split())
        Query.append((l-1,r-1))
    ans=[]
    for l,r in Query:
        box=X[:l]+X[r+1:]
        box.sort()
        dp=[0]*(M+1)
        for i in range(N):
            w,v=W[i],V[i]
            for j in range(M-1,-1,-1):
                if box[j]>=w:
                    dp[j+1]=max(dp[j+1],dp[j]+v)
        ans.append(max(dp))
    print('\n'.join(map(str,ans)))
solve()

=======
Suggestion 5

def solve():
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
        Query.append([l,r])
    for i in range(Q):
        l = Query[i][0]
        r = Query[i][1]
        X_tmp = X[:l-1] + X[r:]
        X_tmp.sort()
        ans = 0
        for j in range(N):
            for k in range(len(X_tmp)):
                if W[j] <= X_tmp[k]:
                    ans += V[j]
                    X_tmp.pop(k)
                    break
        print(ans)
solve()

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    W = []
    V = []
    for i in range(N):
        w, v = map(int, input().split())
        W.append(w)
        V.append(v)
    X = list(map(int, input().split()))
    Query = []
    for i in range(Q):
        l, r = map(int, input().split())
        Query.append([l, r])
    for i in range(Q):
        l, r = Query[i]
        X_temp = X[:l-1] + X[r:]
        W_temp = W[:]
        V_temp = V[:]
        ans = 0
        for j in range(len(X_temp)):
            max_value = 0
            max_index = 0
            for k in range(len(W_temp)):
                if W_temp[k] <= X_temp[j] and V_temp[k] > max_value:
                    max_value = V_temp[k]
                    max_index = k
            if max_value > 0:
                ans += max_value
                W_temp.pop(max_index)
                V_temp.pop(max_index)
        print(ans)

=======
Suggestion 7

def solve():
    N, M, Q = map(int, input().split())
    W = [0] * (N + 1)
    V = [0] * (N + 1)
    for i in range(1, N + 1):
        W[i], V[i] = map(int, input().split())
    X = [0] * (M + 1)
    X[1:] = list(map(int, input().split()))
    for _ in range(Q):
        L, R = map(int, input().split())
        res = 0
        for i in range(1, L):
            res += V[i]
        for i in range(R + 1, M + 1):
            res += V[i]
        dp = [[0] * (N + 1) for _ in range(X[L] + 1)]
        for i in range(1, N + 1):
            for j in range(X[L], W[i] - 1, -1):
                dp[j][i] = max(dp[j][i - 1], dp[j - W[i]][i - 1] + V[i])
            for j in range(X[L] - W[i], -1, -1):
                dp[j][i] = max(dp[j][i - 1], dp[j + W[i]][i - 1] + V[i])
        res += dp[0][N]
        print(res)

=======
Suggestion 8

def dp(n, m, q, w, v, x, query):
    dp = [[0 for i in range(100)] for j in range(100)]
    for i in range(n):
        for j in range(m):
            for k in range(100):
                if k - w[i] >= 0:
                    dp[i+1][j+1][k] = max(dp[i][j+1][k], dp[i][j][k-w[i]] + v[i])
                else:
                    dp[i+1][j+1][k] = dp[i][j+1][k]
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(100):
                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k])
    for i in range(q):
        ans = 0
        for j in range(query[i][0], query[i][1]+1):
            ans += x[j-1]
        print(dp[n][m][ans])

n, m, q = map(int, input().split())
w = [0 for i in range(n)]
v = [0 for i in range(n)]
x = [0 for i in range(m)]
for i in range(n):
    w[i], v[i] = map(int, input().split())
for i in range(m):
    x[i] = int(input())
query = [[0 for i in range(2)] for j in range(q)]
for i in range(q):
    query[i][0], query[i][1] = map(int, input().split())
dp(n, m, q, w, v, x, query)

=======
Suggestion 9

def main():
    N,M,Q = map(int,input().split())
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    X = list(map(int,input().split()))
    Query = [0] * Q
    for i in range(Q):
        Query[i] = list(map(int,input().split()))
    for i in range(Q):
        L = Query[i][0]
        R = Query[i][1]
        X_temp = X[0:L-1] + X[R:]
        X_temp.sort()
        V_temp = V[0:L-1] + V[R:]
        V_temp.sort()
        W_temp = W[0:L-1] + W[R:]
        W_temp.sort()
        print(X_temp)
        print(V_temp)
        print(W_temp)
        print('**********')
        Sum = 0
        j = 0
        while j < len(X_temp):
            Sum += V_temp[j]
            j += 1
        print(Sum)

=======
Suggestion 10

def main():
    n, m, q = map(int, input().split())
    wv = [list(map(int, input().split())) for _ in range(n)]
    x = list(map(int, input().split()))
    query = [list(map(int, input().split())) for _ in range(q)]

    for i in range(q):
        l, r = query[i][0], query[i][1]
        xx = x[:l-1] + x[r:]
        xx.sort()
        res = 0
        for j in range(n):
            for k in range(len(xx)-1, -1, -1):
                if wv[j][0] <= xx[k]:
                    res += wv[j][1]
                    xx.pop(k)
                    break
        print(res)
