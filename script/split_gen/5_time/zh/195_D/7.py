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
