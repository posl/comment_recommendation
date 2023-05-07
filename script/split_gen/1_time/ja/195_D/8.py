def solve():
    N,M,Q = map(int,input().split())
    W = [0]*N
    V = [0]*N
    for i in range(N):
        W[i],V[i] = map(int,input().split())
    X = [0]*M
    for i in range(M):
        X[i] = int(input())
    query = [0]*Q
    for i in range(Q):
        L,R = map(int,input().split())
        L -= 1
        R -= 1
        query[i] = (L,R)
    for L,R in query:
        #箱の大きさのリストを作る
        x = []
        for i in range(M):
            if i < L or R < i:
                x.append(X[i])
        #箱の大きさのリストを使って、各荷物の価値の合計の最大値を求める
        dp = [0]*(sum(x)+1)
        for i in range(N):
            for j in range(sum(x),W[i]-1,-1):
                dp[j] = max(dp[j],dp[j-W[i]]+V[i])
        print(max(dp))
solve()
