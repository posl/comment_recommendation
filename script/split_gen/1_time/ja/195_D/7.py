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
